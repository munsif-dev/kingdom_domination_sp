import socket
from _thread import *
import pickle
from game import Game

server = "192.168.177.2"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    print(str(e))

s.listen()
print("Waiting for a connection, Server Started")

connected = set()
games = {}
idCount = 0

def threaded_client(conn, player, gameId):
    global idCount
    conn.send(str.encode(str(player)))

    reply = ""
    while True:
        try:
            data = conn.recv(4096).decode()

            if gameId in games:
                game = games[gameId]

                if not data:
                    break
                else:
                    if data == "reset":
                        game.resetWent()
                    elif data != "get":
                        game.play(player, data)

                    conn.sendall(pickle.dumps(game))
            else:
                break
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

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    idCount += 1
    p = (idCount - 1) % 3  # Player number 0, 1, or 2
    gameId = (idCount - 1) // 3  # Grouping players into games of 3
    if idCount % 3 == 1:
        games[gameId] = Game(gameId)
        print("Creating a new game... game ID:", gameId)
    else:
        if idCount % 3 == 0:
            games[gameId].ready = True  # The game starts when the third player joins
            p = 2

    start_new_thread(threaded_client, (conn, p, gameId))
