import socket
from _thread import start_new_thread
import pickle
from game import Game

def threaded_client(conn, player, gameId):
    global idCount
    print(str.encode(str(player)))
    conn.send(str.encode(str(player)))
    
    while True:
        try:
            data = conn.recv(4096).decode()
            print(data)
            if not data:
                break
            if data.startswith("get"):
                response= pickle.dumps(games[gameId])
                print("response", response)
                conn.sendall(response)
                print("Sending game state") # Debugging
            elif data.startswith("get_question"):
                _, index = data.split()
                question = games[gameId].get_question(int(index))
                conn.sendall(pickle.dumps(question))
            elif data.startswith("answer"):
                _, index, answer = data.split()
                correct = games[gameId].answer_question(int(index), player, answer)
                conn.sendall(pickle.dumps(correct))
        except:
            break

    print("Lost connection")
    try:
        del games[gameId]
        print("Closing Game", gameId)
    except:
        pass
    idCount -= 1
    conn.close()

server = "192.168.177.2"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    print(str(e))

s.listen(2)
print("Waiting for a connection, Server Started")

connected = set()
games = {}
idCount = 0

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    idCount += 1
    gameId = (idCount - 1) // 2
    if idCount % 2 == 1:
        games[gameId] = Game(gameId)
        print("Creating a new game...")
    else:
        games[gameId].ready = True

    start_new_thread(threaded_client, (conn, idCount % 2, gameId))
