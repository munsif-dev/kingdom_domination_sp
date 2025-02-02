import socket
import pickle

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.33.2"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def getP(self):
        return self.p

    def connect(self):
        try:
            print(self.addr)
            self.client.connect(self.addr)
            player_info = self.client.recv(2048).decode()  # Decode the bytes object
            print("Received player info:", player_info)
            return int(player_info)  # Convert from string to int
        except Exception as e:
            print(f"Failed to connect: {e}")
            return None

   

    def send(self, data):
        try:
            self.client.sendall(data.encode())  # Sending the request to the server
            response = self.client.recv(4096)  # Receiving the response
           
            return response
        except Exception as e:
            print("Network error:", e)
            return None