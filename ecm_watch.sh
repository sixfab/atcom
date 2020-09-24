#!/usr/bin/env bash

INTERFACE=${1:-"usb0"}

#echo $INTERFACE

lsusb | grep Quectel >> /dev/null
IS_QUECTEL=$?

lsusb | grep Telit >> /dev/null
IS_TELIT=$?

echo $IS_QUECTEL
echo $IS_TELIT

if [[ $IS_QUECTEL -eq 0 ]]; then

    INTERFACE="usb0"
    echo "Default Interface for Quectel ECM Mode: " $INTERFACE

    ifconfig | grep wwan0 >> /dev/null 
    INTERFACE_WWAN=$?

    ifconfig | grep usb0 >> /dev/null
    INTERFACE_USB=$?

    if [[ $INTERFACE_USB -eq 1 ]] && [[ $INTERFACE_WWAN -eq 1 ]]; then
        # There is no modem interface
        # Reboot the modem to solve this

        echo $(date "+%H:%M:%S - %Y/%m/%d :") "Modem restarting..."
        python3 at_test.py AT+CFUN=1,1 OK ERROR
    fi
fi

if [[ $IS_TELIT -eq 0 ]]; then
    INTERFACE="wwan0"
    echo "Default Interface for Telit ECM Mode: " $INTERFACE
fi

while true ; do
	
    # Control cellular internet connection
    ping -c 2 -s 0 -I $INTERFACE 8.8.8.8 >> /dev/null
    PINGI=$?
    ping -c 2 -s 0 8.8.8.8 >> /dev/null
    PINGG=$? 

    echo "PINGI: " $PINGI "PINGG: " $PINGG

	if [[ $PINGI -eq 0 ]] && [[ $PINGG -eq 0 ]]; then
		ifconfig | grep wlan0 >> /dev/null
		if [[ $? -eq 0 ]]; then
			# sudo ifconfig wlan0 down
			echo $(date "+%H:%M:%S - %Y/%m/%d :") "Wifi turned OFF"
        else
            # wifi is already turned off
            echo "wifi is already off"
		fi
	else
        echo $(date "+%H:%M:%S - %Y/%m/%d :") "Cellular connection is lost. Testing modem configurations..."
        python3 at_test.py AT+CREG? OK ERROR
        python3 at_test.py AT+CGREG? OK ERROR
        python3 at_test.py AT+COPS? OK ERROR
        python3 at_test.py AT+CGDCONT? OK ERROR
        echo $(date "+%H:%M:%S - %Y/%m/%d :") "Modem restarting..."
        python3 at_test.py AT+CFUN=1,1 OK ERROR
        
		sleep 60 # wait until modem is restarted

        if [[ $IS_TELIT -eq 0 ]]; then
            python3 at_test.py "AT#ECM=1,0,\"\",\"\",0" "OK" "ERROR"
            sleep 10 # wait until ECM start
        fi 

        if ping -c 2 -s 0 -I $INTERFACE 8.8.8.8 >> /dev/null; then
            echo $(date "+%H:%M:%S - %Y/%m/%d :") "Cellular connection restored..."
		else
			ifconfig | grep wlan0 >> /dev/null
			if [[ $? -ne 0 ]]; then
			# sudo ifconfig wlan0 up
			echo $(date "+%H:%M:%S - %Y/%m/%d :") "wifi turned ON for 1 minute"
			sleep 1m
			fi
        fi
	fi
	sleep 10
done
 