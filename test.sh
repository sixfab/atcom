#!/usr/bin/env bash

INTERFACE=${1:-"usb0"}

echo $INTERFACE

while(true) ; do
	
    # Control cellular internet connection
	if ping -c 1 -I $INTERFACE 8.8.8.8 >> /dev/null; then
		ifconfig | grep wlan0 >> /dev/null
		if [[ $? -eq 0 ]]; then
			# sudo ifconfig wlan0 down
			echo wifi turned OFF ------------------- $(date "+%H:%M:%S - %Y/%m/%d")  
		fi
	else
        echo "Cellular conn ection is lost. Testing modem configuraitons..."
        python3 at_test.py AT+CREG? OK ERROR
        python3 at_test.py AT+CGREG? OK ERROR
        python3 at_test.py AT+COPS? OK ERROR
        python3 at_test.py AT+CGDCONT? OK ERROR
        echo "modem restarting..."
        python3 at_test.py AT+CFUN=1,1 OK ERROR
        
		sleep 60 # wait until modem is restarted
		
        if ping -c 1 -I $INTERFACE 8.8.8.8 >> /dev/null; then
            echo "Cellular connection restored..."
		else
			ifconfig | grep wlan0 >> /dev/null
			if [[ $? -ne 0 ]]; then
			# sudo ifconfig wlan0 up
			echo wifi turned ON  ------------------- $(date "+%H:%M:%S - %Y/%m/%d")
			echo "wifi activated for 5 minutes"
			sleep 5m
			fi
        fi
	fi
	sleep 10
done