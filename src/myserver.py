# tis is the listener for the humidity sensor
# ak march 2026



import socket #get the socket library
import ast  

DEBUG = False
class MyServer(object):


    def __init__(self, host='localhost', port=5000):
        
        
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        self.sock.listen(1)
        print(f"Server listening on {self.host}:{self.port}")

    def start(self):
        while True:
            conn, addr = self.sock.accept()
            if(DEBUG):
                print(f"Connection from {addr}")
            data = conn.recv(1024).decode('utf-8')
            if(DEBUG):
                print(f"Received data: {data}")
            # Evaluate the received data as a Python literal
            try:
                self.mydata = ast.literal_eval(data)
                if(DEBUG):
                    print(f"Evaluated data: {self.mydata}")
            except (ValueError, SyntaxError):
                print("Received invalid data")


            conn.close()

if __name__ == "__main__":
    host = socket.gethostname()
    server = MyServer(host='192.168.3.150', port=9378)
    server.start()