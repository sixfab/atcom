from subprocess import check_output
from .modems import supported_modems


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
            elif line.startswith("ID_VENDOR_ID="):
                _port_details["vendor_id"] = line[13:].replace("'", "")
            elif line.startswith("ID_MODEL="):
                _port_details["model"] = line[9:].replace("'", "")
            elif line.startswith("ID_MODEL_FROM_DATABASE="):
                _port_details["model_from_database"] = line[23:].replace("'", "")
            elif line.startswith("ID_MODEL_ID="):
                _port_details["product_id"] = line[12:].replace("'", "")
            elif line.startswith("ID_USB_INTERFACE_NUM="):
                _port_details["interface"] = "if"+line[21:].replace("'", "")

        if "bus" not in _port_details["port"]:
            available_ports.append(_port_details)

    return available_ports


def find_cellular_modem():
    """function to find supported modem"""
    output = check_output("lsusb", shell=True).decode()

    for modem in supported_modems:
        if output.find(modem.vid) != -1 and output.find(modem.pid) != -1:
            return modem
    raise Exception("No supported modem exist!")


def decide_port():
    """function to decide port name of supported modem"""
    try:
        modem = find_cellular_modem()
    except:
        return (None, None)
    else:
        ports = get_available_ports()
        for port in ports:
            if  modem.com_ifs in port.values() and \
                modem.vid in port.values() and \
                modem.pid in port.values():
                
                port_name = port.get("port")
                modem.desc_vendor = port.get("vendor")
                modem.desc_product = port.get("model", port.get("model_from_database"))
                return (port_name, modem)
        return (None, None)
