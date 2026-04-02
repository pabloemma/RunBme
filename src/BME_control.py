# this is the code which runs on the raspberry pi connected to the BME280
#it mainly runs the read loop and communicates with the server


import time
import MyClient as MY
import ReadBme as RB

class BMEControl(object):
    def __init__(self,host = '192.168.3.150', port = 9378,sleep_time = None):
        self.host = host
        self.port = port

        self.bme = RB.ReadBme()
        self.client = MY.MyClient(host=self.host)
        self.client.connect()#setup connection to server

        if sleep_time == None:
            self.sleep_time = 60


    def run(self):
        while True:
            data = self.bme.read_short()
            #print(data)
            #self.client.send('happy hour')
            self.client.connect()
            self.client.send(str(data))
            # Send data to server
            time.sleep(self.sleep_time)

if  __name__ == "__main__":
    host = '192.168.3.150'
    port = 9378

    bme_control = BMEControl(host=host, port=port)
                             
    bme_control.run()
