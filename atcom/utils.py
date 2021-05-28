from subprocess import check_output
from .modems import supported_modems

def find_cellular_modem():
    """function to find supported modem"""
    output = check_output("lsusb", shell=True).decode()

    for modem in supported_modems:
        if output.find(modem.vid) != -1 and output.find(modem.pid) != -1:
            return modem
    raise Exception("No supported modem exist!")


def find_modem_description(modem):
    """function to get vendor name and product name on kernel driver"""
    output = check_output("usb-devices", shell=True).decode().split("\n")
    for line in output:
        if line.find(modem.vid) != -1:
            desc_man_line = output.index(line)+1
            desc_prod_line = output.index(line)+2
            modem.desc_vendor = output[desc_man_line].split("=")[1]
            modem.desc_product = output[desc_prod_line].split("=")[1]
            return
    raise Exception("Modem description couldn't find!")
    

def decide_port():
    """function to decide port name of supported modem"""
    try:
        modem = find_cellular_modem()
    except:
        return (None, None)
    else:
        try:
            find_modem_description(modem)
        except:
            # Skip descripter control
            modem.desc_vendor = ""
            modem.desc_product = ""

        output = check_output("ls -l /dev/serial/by-id", shell=True).decode().split("\n")
        for line in output:
            if line.find(modem.com_ifs) != -1 and line.find(modem.desc_vendor) != -1 and line.find(modem.desc_product) != -1 :
                start = line.find("tty")
                port_name = "/dev/" + line[start:]
                return (port_name, modem)
        return (None, None)
