# tis is the listener for the humidity sensor
# ak march 2026



import socket #get the socket library
import ast  
import SetupBME as S_BME
import CreatePandas as C_Pandas


class MyServer(object):


    def __init__(self, host='localhost', port=5000):
        

        # get configuration file
        self.config = S_BME.SetupBME()
        self.config.get_config()

        #setup Pandas
        self.pandas_ak = C_Pandas.MyPandas(column_names = self.config.column_names, output_dir = self.config.output_dir)
        self.pandas_ak.CreateFileName()
        self.pandas_ak.CreateFrame()


                               
        
        self.host = self.config.server_ip
        self.port = self.config.server_port
        self.DEBUG = self.config.DEBUG

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        self.sock.listen(1)
        print(f"Server listening on {self.host}:{self.port}")

    def start(self):
        while True:
            conn, addr = self.sock.accept()
            if(self.DEBUG):
                print(f"Connection from {addr}")
            data = conn.recv(1024).decode('utf-8')
            if(self.DEBUG):
                print(f"Received data: {data}")
            # Evaluate the received data as a Python literal
            try:
                self.mydata = ast.literal_eval(data)
                if(self.DEBUG):
                    print(f"Evaluated data: {self.mydata}")
                    self.pandas_ak.AddData(self.mydata) 

                    
            except (ValueError, SyntaxError):
                print("Received invalid data")


            conn.close()

if __name__ == "__main__":
    host = socket.gethostname()
    server = MyServer(host='192.168.3.150', port=9378)
    server.start()