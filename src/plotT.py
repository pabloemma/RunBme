import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import sys

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
    temp= 'Temperature_'+b+'_.csv'
else:
    temp = 'Temperature_'+mydate+'_.csv'
myfile =str(Path.home())+'/scratch/'+temp
myfile = '/Users/klein/git/RunBme/data/BME280_2026-04-03_.csv'
data = pd.read_csv(myfile,index_col=0,parse_dates=True)
#temp = data['temperature']*1.8+32
temp = data['temperature']
temp1 = data['pressure']/30.0 #to keep pressute on same plot
temp2 = data['humidity']
temp3 = data['temperature']*1.8+32

#temp.plot()
#temp.plot(ax=ax,marker='+',color='green',linestyle='None')
temp.plot(ax=ax,color='green',linestyle='--')
temp1.plot(ax=ax,color='red',linestyle='--')
temp2.plot(ax=ax,color='blue',linestyle='--')
temp3.plot(ax=ax,color='black',linestyle='--')                      


#This could also be done using
#ax.setp(temp,linestyle='--')




plt.ylim(15.,100.)

ax.set_ylabel("Temperature")
ax.set_title("living room T")
ax.text(75., .025,r'$\sigma_i=15$')
ax.grid(True)


plt.show()






