from subprocess import check_output
from .modems import modems

def get_available_ports():
    ports = check_output("find /sys/bus/usb/devices/usb*/ -name dev", shell=True)
    ports = ports.decode().split("\n")

    available_ports = []

    for port in ports:
        if port.endswith("/dev"):
            port = port[:-4]

        if not port:
            continue

        try:
            device_details = check_output("udevadm info -q property --export -p {}".format(port), shell=True)
        except:
            continue

        device_details = device_details.decode().split("\n")

        _port_details = {}

        for line in device_details:
            if line.startswith("DEVNAME="):
                _port_details["port"] = line[8:].replace("'", "")
            elif line.startswith("ID_VENDOR="):
                _port_details["vendor"] = line[10:].replace("'", "")
            elif line.startswith("ID_MODEL="):
                _port_details["model"] = line[9:].replace("'", "")
            elif line.startswith("ID_USB_INTERFACE_NUM="):
                _port_details["interface"] = line[21:].replace("'", "")

        if "bus" not in _port_details["port"]:
            available_ports.append(_port_details)

    return available_ports


def decide_port():
    ports = get_available_ports()

    for port in ports:
        for modem_name, interfaces in modems.items():
            if modem_name in port["model"] and port["interface"] in interfaces:
                return port["port"]

    return None
