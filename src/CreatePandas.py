import pandas as pd
import matplotlib as mp
import datetime as dt
import sys
import json
import os
#import nextcloud_transfer as nt
import time

class MyPandas(object):

    def __init__(self,column_names = None, output_dir = None ,altitude = None ):

        
        print("welcome to the world of pandas")
        self.data_list = ([0.,0.,0.,0.,0.])

        if altitude is None:
            self.altitude = 255
        else:
            self.altitude = altitude

        if(column_names is None):
            self.column_names = ['time','temperature','humidity','pressure','altitude']            
        else:
            self.column_names = column_names.split(',') # we expect a string with comma separated column names          
        if(output_dir is None):
            print('output directory missing, exiting')           
            sys.exit(1)
        else:
            self.output_dir = output_dir

    


    def CreateFrame(self):

        self.MyFrame = pd.DataFrame(columns = self.column_names)
        print(self.MyFrame)
        # write to file , we choose csv file
        if os.path.exists(self.file_out):
            pass # no , in the beginning
        else:
            self.MyFrame.to_csv(self.file_out,index=False,mode='w') # no , in the beginning
 

    def CreateFileName(self):
        '''creates filename based on date'''
        
        a = dt.datetime.today().strftime('%Y-%m-%d')
        
        self.file_out =self.output_dir+'BME280_' + a+'_.csv'  #add hostname
        return
        


    def AddData(self,data):
        '''adds a row of data to the end'''

        # check time if we are close to midnight we create a new file


        self.data_list = list(data.values())
        # add time to the data
        a=dt.datetime.now()

        self.data_list.insert(0,a)

        # now correct pressure
        self.CorrectAltitude(self.data_list[3],self.altitude)



        if not self.FlushTime():
            
            #first read file
            temp = pd.read_csv(self.file_out)
            temp.loc[temp.index.max()+1] = self.data_list 
                 # write it out again
            temp.to_csv(self.file_out,index = False)


        elif self.FlushTime():

            time.sleep(17*60)
            
            self.CreateFileName()
            self.MyFrame.to_csv(self.file_out,index=False,mode='w') # no , in the beginning
         
               # now write to nextcloud
        #self.nx.upload_file(file_path_in = self.file_out , upload_dir = self.nextcloud_dir)
           
    def FlushTime(self):
        
        """
        checks time and if its close tp midnight returns True
        """
        timelimit = 23*60.+ 45  # this is how many minutes are to 23:45
        #timelimit = 7*60.+ 40  # this is how many minutes are to 23:45
        
        #tomorrow = (dt.datetime.today()+dt.timedelta(1)).strftime('%Y-%m-%d')


        b=  dt.datetime.now()
        #fill in tuple
        a=b.timetuple()
        current_minute = a[3]*60. + a[4]
        
        if(current_minute > timelimit):
            return True
        else:
            return False
    def CorrectAltitude(self,pressure,altitude):
        '''corrects pressure for altitude'''
        
        p0 = pressure / (1 - (altitude / 44330.0)) ** 5.255
        return p0

        return P


if __name__ == "__main__":


    config_file = '/Users/klein/git/Thermostat/config/temp.json'
    MyP = MyPandas(config_file=config_file)
    MyP.CreateFrame()
    a=dt.datetime.now()
    data_list = [a,54,987,66]
    MyP.AddData(data_list)