# this is the code which runs on the raspberry pi connected to the BME280
#it mainly runs the read loop and communicates with the server


import time
import MyClient as MY
import ReadBme as RB

class BMEControl(object):
    def __init__(self,host = 'localhost', port = 9378):
        self.bme = RB.ReadBme()
        self.client = MY.MyClient()
        self.client.connect()#setup connection to server




    def run(self):
        while True:
            data = self.bme.read_short()
            print(data)
            self.client.send(str(data))
            # Send data to server
            time.sleep(2)

if  __name__ == "__main__":
    host = '192.168.3.150'
    port = 9378

    bme_control = BMEControl(host=host, port=port)
                             
    bme_control.run()
