# ATCom
​
AT commands are the instructions used to control and communicate with the cellular modems. In order to, send AT commands to a cellular device, one needs to check several parameters and might need a serial monitor tool. 
ATCom is a command-line interface tool that makes AT command operations easier.
​
## Installation
​
[pip3](https://pip.pypa.io/en/stable/) is required to install the **atcom**. pip3 can be intalled by 
​
```bash
sudo apt install python3-pip
```
​
Use the package manager [pip3](https://pip.pypa.io/en/stable/) to install **atcom**.
​
```bash
pip3 install atcom
```
​
## Usage
​
```bash
$ atcom [OPTIONS] AT_COMMAND
```
​
### Examples
​
Running **atcom** without *--port* parameter, scans for available ports, and selects a valid modem port if available.
​
```bash
$ atcom AT
```
​
or
​
```bash
$ atcom --port /dev/ttyUSB2 AT
```
​
## Configuration File
​
Configuration file(configs.yaml) can be created for persist args. 
ATCom first checks the current working directory for the configs.yml to read the arguments from. The path of the configuration file can also be specified using the **--config** parameter. 
​
The configuration file must be in *yaml* format, for example: 
​
```yaml
port: /dev/ttyUSB2
baudrate: 115200
timeout: 10
```
​
The keys, config file can contain:
* port (str)
* baudrate (int)
* timeout (int)
* rts_cts (boolean)
* dsr_dtr (boolean)
* verbose (boolean)
​
### Parameters
​
|                 |     default    |            description           |
|-----------------|:--------------:|:--------------------------------:|
| -p / --port     |        -       | PORT of modem                    |
| -b / --baudrate |     115200     | Baudrate for serial communication|
| -t / --timeout  |        10      | Communication timeout            |
| -c / --config   | ./configs.yaml | Configurations file Path         |
| -v / --verbose  |        -       | Enable full log output           |
| --rts-cts       |        -       | Enable RTS-CTS mode              |
| --dsr-dtr       |        -       | Enable DSR-DTR mode              |
​
​
## License
[MIT](https://choosealicense.com/licenses/mit/)