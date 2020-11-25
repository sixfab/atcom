# ATCom

ATCom is a command line tool to make AT command operations easier.

## Installation

Use the package manager [pip3](https://pip.pypa.io/en/stable/) to install **atcom**.

```bash
pip3 install atcom
```

## Usage

```bash
$ atcom [OPTIONS] AT_COMMAND
```

### Examples

If you run **atcom** without *--port* parameter, the tool will scan available ports and select a valid modem if it can find.

```bash
$ atcom AT
```

or

```bash
$ atcom --port /dev/ttyUSB2 AT
```

## Configuration File

You can create a configuration file for persist args. ATCom checks current directory first, reads args from config file if you have a configs.yml in **./ (current)** directory. Also you can specify the path of configuration file with **--config** parameter. 

The keys, config file can contain:
* port (str)
* baudrate (int)
* timeout (int)
* rts_cts (boolean)
* dsr_dtr (boolean)
* verbose (boolean)

### Parameters

|                 | need value |       is required      |     default    |            description           |
|-----------------|------------|:----------------------:|:--------------:|:--------------------------------:|
| -p / --port     |     yes    | yes, unless--auto flag |        -       | PORT of modem                    |
| -b / --baudrate |     yes    |           no           |     115200     | Baudrate of serial communication |
| -t / --timeout  |     yes    |           no           |        3       | Communication timeout            |
| -c / --config   |     yes    |           no           | ./configs.yaml | Path of configurations file      |
| -v / --verbose  |     no     |           no           |        -       | Enable full log output           |
| --rts-cts       |     no     |           no           |        -       | Enable RTS-CTS mode              |
| --dsr-dtr       |     no     |           no           |        -       | Enable DSR-DTR mode              |


## License
[MIT](https://choosealicense.com/licenses/mit/)