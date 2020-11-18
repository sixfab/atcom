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

You can use **--auto** flag to detect modem port automatically. If the tool couldn't detect your modem, you can specify the port manually with **--port** parameter.

```bash
$ atcom --auto AT
```

or

```bash
$ atcom --port /dev/ttyUSB2 AT
```

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
| --auto          |     no     |           no           |        -       | Scan ports automatically         |

## License
[MIT](https://choosealicense.com/licenses/mit/)