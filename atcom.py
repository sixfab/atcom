#!/usr/bin/python3

"""
  Sixfab atcom API 
  -
  API for AT communication for Sixfab LTE modules. 
  -
  Created by Yasin Kaya (selengalp), September 14, 2020.
"""

import time
import serial

# global variables
TIMEOUT = 3 # seconds
ser = serial.Serial()

###########################################
### Private Methods #######################
###########################################

# Function for printing debug message 
def debug_print(message):
	print(message)

# Function for getting time as miliseconds
def millis():
	return int(time.time())

# Function for delay as miliseconds
def delay(ms):
	time.sleep(float(ms/1000.0))

###############################################
### ATCom Class ###############################
###############################################

class ATCom:
	""" 
    Sixfab AT Communication API Class.
    
    """   
	timeout = TIMEOUT # default timeout for function and methods on this library.
	
	response = "" # variable for modem self.responses
	compose = "" # variable for command self.composes
	
    # Special Characters
	CTRL_Z = '\x1A'
	
	# Initializer function
	def __init__(self, serial_port="/dev/ttyUSB2", serial_baudrate=115200, module="Quectel EC25", rtscts=False, dsrdtr=False):
		self.module = module
		ser.port = serial_port
		ser.baudrate = serial_baudrate
		ser.parity=serial.PARITY_NONE
		ser.stopbits=serial.STOPBITS_ONE
		ser.bytesize=serial.EIGHTBITS
		ser.rtscts=rtscts
		ser.dsrdtr=dsrdtr
		debug_print(self.module + " initialized!")
			
	def __del__(self): 
		ser.close()
		ser.__del__()
		
 	# Function for clearing global compose variable 
	def clear_compose(self):
		self.compose = ""
	
	# Function for getting modem response
	def get_response(self, desired_response, errors):
		"""Function for getting modem response
        
        Parameters
        -----------	
		desired_response : str
        Success message of modem

		errors : str[]
        Error messages of modem	

        timeout : int [seconds]
        timeout while receiving the response (default is TIMEOUT)

        Returns
        ------- 
        response : str 
        Actual message that received from modem  
        """

		if (ser.isOpen() == False):
			ser.open()
		while 1:	
			self.response =""
			while(ser.inWaiting()):
				self.response += ser.read(ser.inWaiting()).decode('utf-8', errors='ignore')
			
			if(self.response.find(desired_response) != -1):
				#debug_print(self.response)
				return self.response
			
			for err_msg in errors:
				if(self.response.find(err_msg) != -1):
					raise RuntimeError("Module responsed with an error message!")
	
	# Function for sending at comamand to module
	def send_at_comm_once(self, command):
		"""Function for sending AT commmand to modem
        
        Parameters
        -----------	
		command : str
        message that sent to modem 
        """
		if (ser.isOpen() == False):
			ser.open()		
		self.compose = ""
		self.compose = str(command) + "\r"
		ser.reset_input_buffer()
		ser.write(self.compose.encode())
		#debug_print(self.compose)
		
	# Function for sending at command to BG96_AT.
	def send_at_comm(self, command, desired_response, err_messages, timeout = None):
		"""Function for sending/getting AT command/response to/from modem
        
        Parameters
        -----------	
		command : str
        Success message of modem

		desired_response : str
        Success message of modem

		err_messages : str[]
        Error messages of modem	

        timeout : int [seconds]
        timeout while receiving the response (default is TIMEOUT)

        Returns
        ------- 
        response : str 
        Actual message that received from modem  
        """
		
		if timeout is None:
			timeout = self.timeout

		self.send_at_comm_once(command)
		
		self.response =""
		timer = millis()
		while 1:
			if( millis() - timer < timeout): 
				while(ser.inWaiting()):
					try: 
						self.response += ser.read(ser.inWaiting()).decode('utf-8', errors='ignore')
						delay(100)
					except Exception as e:
						debug_print(e.Message)

				if(self.response.find(desired_response) != -1):
					return self.response
				
				else:
					for x in err_messages:
						if(self.response.find(x) != -1):
							raise RuntimeError("Module responsed with error message --> " + str(x))
			else:
				raise TimeoutError("timeout!")
			
