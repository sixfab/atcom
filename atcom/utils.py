from subprocess import check_output
from .modems import supported_modems

def find_cellular_modem():
    output = check_output("lsusb", shell=True).decode()

    for modem in supported_modems:
        if output.find(modem.vid) != -1 and output.find(modem.pid) != -1:
            return modem
    raise Exception("No supported modem exist!")


def decide_port():
    try:
        modem = find_cellular_modem()
    except:
        return None
    else:
        output = check_output("ls -l /dev/serial/by-id", shell=True).decode().split("\n")
        for line in output:
            if line.find(modem.com_ifs) != -1:
                start = line.find("tty")
                port_name = "/dev/" + line[start:]
                return port_name
        return None
