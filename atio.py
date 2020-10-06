#!/usr/bin/python3

from atcom import ATCom
import sys

at = ATCom()

try:
    response = at.send_at_comm(sys.argv[1],sys.argv[2], sys.argv[3])
except RuntimeError as err:
    print(str(err))
except TimeoutError as err:
    print(str(err))
else:
    print(response)