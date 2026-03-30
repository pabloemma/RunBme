# this is the code which runs on the raspberry pi connected to the BME280
#it mainly runs the read loop and communicates with the server


import time
import MyClient as MY
import ReadBme as RB

class BMEControl(object):
    def __init__(self):
        self.bme = RB.ReadBme()
        self.client = MY.MyClient()


    def run(self):
        while True:
            data = self.bme.read_short()
            # Send data to server
            time.sleep(2)

if  __name__ == "__main__":
    bme_control = BMEControl()
    bme_control.run()
