
#!/bin/bash
 


if [ $(ps -efa | grep -v grep | grep BME_control.py -c) -gt 0 ] ;
then
    echo "Process running ...";
else
#temporary if program dies download all the necessary programs
#cd /home/pi/git/speedtest/src
#./update_speedtest
#cd ~
/home/pi/activate_venv.sh
python3 -u /home/pi/git/RunBme/src/BME_control.py  > /home/pi/BME_control.log 2>> /home/pi/BME_control_restart_error.log &


echo "Starting the process";
fi;
