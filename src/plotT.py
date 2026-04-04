import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import sys
import platform
import os
import getpass


       # get configuration file
if platform.system() == 'Darwin':
    my_output_dir = '/Users/'+getpass.getuser()+'/git/RunBme/data/'   #use getpass because of visual code issue on mac
elif platform.system() == 'Linux':
    my_output_dir = '/home/'+os.getlogin()+'/git/RunBme/data/'   
else:
    print('unknown system, exiting')
    exit(1) 



#print(sys.argv[0])
if(len(sys.argv) ==2):
    mydate = sys.argv[1]
    print('plotting for  ',sys.argv[1])
else:
    mydate = 'Today'

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
#mydate = '2024-01-12'
#mydate = 'Today'        
if mydate == 'Today':
    a=dt.datetime.now()
    b=dt.datetime.strftime(a,"%Y-%m-%d")
    temp= 'BME280_'+b+'_.csv'
else:
    temp = 'BME280_'+mydate+'_.csv'
#myfile =str(Path.home())+'/scratch/'+temp
myfile = my_output_dir + temp
#myfile = '/home/klein/git/RunBme/data/BME280_2026-04-04_.csv'
data = pd.read_csv(myfile,index_col=0,parse_dates=True)
#temp = data['temperature']*1.8+32
temp = data['temperature']
temp1 = data['pressure']/30.0 #to keep pressute on same plot
temp2 = data['humidity']
temp3 = data['temperature']*1.8+32

#temp.plot()
#temp.plot(ax=ax,marker='+',color='green',linestyle='None')
temp.plot(ax=ax,color='green',linestyle='--',label ='temperature in C')
temp1.plot(ax=ax,color='red',linestyle='--',label='pressure in hPa divided by 30')
temp2.plot(ax=ax,color='blue',linestyle='--',label='humidity in %')
temp3.plot(ax=ax,color='black',linestyle='--', label ='temperature in F') 
#temp3.plot(ax=ax,color='black', label ='temperature in F') 
ax.legend(loc='upper left')                     


#This could also be done using
#ax.setp(temp,linestyle='--')




plt.ylim(15.,100.)

ax.set_ylabel("Temperature")
ax.set_title("living room T")
ax.text(75., .025,r'$\sigma_i=15$')
ax.grid(True)


plt.show()






