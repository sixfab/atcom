#!/usr/bin/python3

from atcom import ATCom
import sys

at = ATCom()

try:
    response = at.send_at_comm(sys.argv[1],sys.argv[2], sys.argv[3])
except RuntimeError:
    print("Runtime Error")
except TimeoutError:
    print("Timeout Error")
else:
    print(response)