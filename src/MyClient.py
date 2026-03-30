# the BME280 client 

import socket

class MyClient(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = None

    def connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))

    def send(self, message):
        if self.sock:
            self.sock.sendall(message.encode('utf-8'))

    def close(self):
        if self.sock:
            self.sock.close()
            self.sock = None


if __name__ == "__main__":
    client = MyClient('192.168.3.150', 9378)
    client.connect()
    client.send("Hello, Server!")
    client.close()