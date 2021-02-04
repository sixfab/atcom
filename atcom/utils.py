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
            elif line.startswith("ID_VENDOR_ID="):
                _port_details["vendor_id"] = line[13:].replace("'", "")
            elif line.startswith("ID_MODEL="):
                _port_details["model"] = line[9:].replace("'", "")
            elif line.startswith("ID_MODEL_FROM_DATABASE="):
                _port_details["model_from_database"] = line[23:].replace("'", "")
            elif line.startswith("ID_USB_INTERFACE_NUM="):
                _port_details["interface"] = line[21:].replace("'", "")

        if "bus" not in _port_details["port"]:
            available_ports.append(_port_details)

    return available_ports


def get_usb_composition(vendor_id):
    lsusb = check_output("lsusb", shell=True).decode()
    lsusb = lsusb.split("\n")

    for line in lsusb:
        for word in line.split(" "):
            if vendor_id in word:
                return word[len(vendor_id)+1:]

    return None


def decide_port():
    ports = get_available_ports()

    for port in ports:
        if "vendor_id" not in port:
            continue
        
        for vendor, modem_data in modems.items():
            if port["vendor_id"] == vendor:
                for modem, composition in modem_data.items():
                    modem_in_model = modem in port.get("model", "")
                    modem_in_database_model = modem in port.get("model_from_database", "")
                    modem_usb_composition = get_usb_composition(vendor)
                    is_bg95 = modem_usb_composition == "0700" and modem == "BG95"
                        
                    if not (modem_in_model or modem_in_database_model or is_bg95):
                        continue
                    if not modem_usb_composition:
                        continue

                    if port["interface"] == composition[modem_usb_composition][0]:
                        return port["port"]

    return None
