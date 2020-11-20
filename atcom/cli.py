#!/usr/bin/python3

import time
import serial
import click
import sys
import os
import yaml

from .__version__ import __version__
from .utils import decide_port

class Logger:
	def __init__(self, verbose=False):
		self.verbose = verbose

	def info(self, text):
		if self.verbose:
			print("[INFO] ", text)

	def error(self, text):
		print("[ERR]  ", text)
		sys.exit(1)


def millis():
	"""
	Function for getting time as miliseconds
	"""
	return int(time.time())


def delay(ms):
	"""
	Function for delay as miliseconds
	"""
	time.sleep(float(ms/1000.0))


class ATCom:
	""" 
    Sixfab AT Communication API Class
    """
	
	def __init__(self, port, baudrate, rts_cts, dsr_dtr, timeout, verbose, logger, **kwargs):
		
		try:
			self.serial = serial.Serial(port, baudrate, rtscts=rts_cts, dsrdtr=dsr_dtr)
		except serial.serialutil.SerialException:
			logger.error("Couldn't open serial communication")
			sys.exit(1)
		
		self.serial.parity=serial.PARITY_NONE
		self.serial.stopbits=serial.STOPBITS_ONE
		self.serial.bytesize=serial.EIGHTBITS
		self.logger = logger

		self.find_in_response = kwargs.get("find_in_response", None)
	

	def get_response(self, timeout):
		"""
		Function for getting modem response
		"""
		if self.serial.isOpen():
			response =""
			timer = millis()
			
			while True:
				delay(100)
				if millis() - timer < timeout: 
					while self.serial.inWaiting():
						try: 
							response += self.serial.read(self.serial.inWaiting()).decode('utf-8')
						except:
							raise RuntimeError("An error occured while reading from serial port")

				else:
					self.logger.error("Timeout, couldn't get response")

				if "OK" in response or "ERROR" in response:

					if self.find_in_response and self.find_in_response in response:
						return {"response": response, "find": True}

					elif self.find_in_response and self.find_in_response not in response:
						return {"response": response, "find": False}
				
					else:
						return response
		else:
			raise RuntimeError("Serial Port is closed or doesn't exist...")


	def send_at_comm_once(self, command):
		"""
		Function for sending AT commmand to modem
        
		params:
			command: str, message that sent to modem
        """
		try:
			if (self.serial.isOpen() == False):
				ret_val = self.serial.open()
		except Exception as e:
			raise RuntimeError("Serial port couldn't be opened!")
		else:
			self.compose = ""
			self.compose = str(command) + "\r"
			try:
				self.serial.reset_input_buffer()
				self.serial.write(self.compose.encode())
			except:
				raise RuntimeError("Occured an error while writing to serial port!")

		
	# Function for sending at command to BG96_AT.
	def send_at_comm(self, command, timeout):
		self.send_at_comm_once(command)
		return self.get_response(timeout)


@click.command()
@click.option('-p', '--port', help='Full path of serial port.', type=str)
@click.option('-b', '--baudrate', help='Baudrate of serial communication.', type=int)
@click.option('-t', '--timeout', help='Command timeout value.', type=int)
@click.option('-c', '--config', help='Full path of config file.', type=str)
@click.option('-f', '--find', help='Find in response, wait until find', type=str)
@click.option('-v', '--verbose', is_flag=True, help='Flag to verbose all processes.')
@click.option('--rts-cts', 'rts_cts', is_flag=True, help="Flag to enable RTS-CTS mode")
@click.option('--version', 'show_version', is_flag=True, help="Show ATCom version")
@click.option('--dsr-dtr', 'dsr_dtr', is_flag=True, help="Flag to enable DSR-DTR mode")
@click.argument('at_command', default="")
def handler(port, baudrate, timeout, verbose, rts_cts, dsr_dtr, config, at_command, show_version, find):
	if show_version:
		print("ATCom version: ", __version__)
		return

	logger = Logger(verbose)
	configs = {}


	if not at_command:
		print("Error: AT_COMMAND missing\n")
		print("Usage: t.py [OPTIONS] AT_COMMAND")
		print("Try 't.py --help' for help.")
		return

	try:
		config_file_path = config or "./configs.yml"

		configs = open(config_file_path, "r").read()
		configs = yaml.load(configs, Loader=yaml.FullLoader)
	
	except FileNotFoundError:
		logger.info("Configs file not found, reading properties from args")

	else:
		logger.info("Found configs file, loading properties")

	properties = (
		{"id": "port", "name": "Port", "required": True},
		{"id": "rts_cts", "name": "RTS-CTS", "required": False},
		{"id": "dsr_dtr", "name": "DSR_DTR", "required": False},
		{"id": "timeout", "name": "Timeout", "required": False}
	)


	for _property in properties:
		if not locals().get(_property["id"], None):
			continue
	
		logger.info("{} property specified as argument, overriding config file".format(_property["name"]))
		configs[_property["id"]] = locals().get(_property["id"])

	if not configs.get("port"):
		logger.info("Port not specified, scanning available ports")
	
		port_to_connect = decide_port()

		if not port_to_connect:
			logger.error("Couldn't find any available port automatically, please specify the port")

		logger.info("Found a modem on {}".format(port_to_connect))
		
		configs["port"] = port_to_connect
		
	for _property in properties:
		if _property["required"] and _property["id"] not in configs:
			logger.error("Property "+ _property["id"]+ " not specified, its required")

	if "timeout" not in configs:
		logger.info("Timeout property not found, using default (10)")
		configs["timeout"] = 10

	if "baudrate" not in configs:
		logger.info("Baudrate property not found, using default (115200)")
		configs["baudrate"] = 115200

	if "rts_cts" not in configs:
		configs["rts_cts"] = rts_cts
	if "dsr_dtr" not in configs:
		configs["dsr_dtr"] = dsr_dtr
	if "verbose" not in configs:
		configs["verbose"] = verbose

	at = ATCom(
		configs["port"], 
		configs["baudrate"], 
		configs["rts_cts"], 
		configs["dsr_dtr"], 
		configs["timeout"], 
		configs["verbose"], 
		logger,
		find_in_response=find
	)

	try:
		response = at.send_at_comm(at_command, configs["timeout"])
		status_code = 0

		if type(response) == dict:
			if response["find"] == False:
				status_code = 1
				logger.info("Couldn't find '{}' in response, exit status code set to 1".format(find))

			response = response["response"]
			
		response_lines = response.split("\n")

		if not response_lines or response_lines == ['']:
			logger.error("Couldn't recieve any response")
			return
		
		if verbose:
			print()

		if len(response_lines) > 1:
			if response_lines[0].startswith("AT"):
				if verbose:
					print("< ", response_lines[0])
					print()
					for line in response_lines[1:]:
						print("> ", line)
				else:
					for line in response_lines:
						print(line)
			else:
				for line in response_lines:
					print(line)
		else:
			print(response[0])

		sys.exit(status_code)

	except RuntimeError as err:
		logger.error(str(err))

	except TimeoutError as err:
		logger.error(str(err))


if __name__ == "__main__":
	cli_handler()
