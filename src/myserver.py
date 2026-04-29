# tis is the listener for the humidity sensor
# ak march 2026



import socket #get the socket library
import ast  
import SetupBME as S_BME
import CreatePandas as C_Pandas
import platform
import datetime as dt
import os
import subprocess
import getpass


class MyServer(object):


    def __init__(self, host='localhost', port=5000, config_file = None, my_output_dir = None):
        

        if host == 'localhost':
            self.host = self.GetMyIp()

        if config_file == None:
        # get configuration file
            if platform.system() == 'Darwin':
                config_file = '/Users/'+getpass.getuser()+'/git/RunBme/config/BME280.json'
                my_output_dir = '/Users/'+getpass.getuser()+'/git/RunBme/data/'   
            elif platform.system() == 'Linux':
                config_file = '/home/'+os.getlogin()+'/git/RunBme/config/BME280.json'
                my_output_dir = '/home/'+os.getlogin()+'/git/RunBme/data/'   
            else:
                print('unknown system, exiting')
                exit(1) 


        self.config = S_BME.SetupBME(config_file=config_file)
        self.config.get_config()



        #setup Pandas
        self.pandas_ak = C_Pandas.MyPandas(column_names = self.config.column_names, output_dir = my_output_dir)
        self.pandas_ak.CreateFileName()
        self.pandas_ak.CreateFrame()


                               
        
        self.host = self.config.server_ip #--- IGNORE ---
        self.port = self.config.server_port
        self.DEBUG = self.config.DEBUG
        self.altitude = self.config.altitude

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

    def GetMyIp(self):
        y = subprocess.run(['/usr/bin/hostname', '-I'], capture_output=True)
        ipAddrs = y.stdout.split()
        ipv4 = ipAddrs[0]
        print(f"My IP address is: {ipv4.decode('utf-8')}")
        return ipv4.decode('utf-8')
    
        

if __name__ == "__main__":
    #host = socket.gethostname()
    config_file = '/home/klein/git/RunBme/config/BME280.json'
    my_output_dir = '/home/klein/git/RunBme/data/'
    server = MyServer(host ='192.168.3.151', port=9378,config_file=config_file, my_output_dir=my_output_dir)
    server.start()