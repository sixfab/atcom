#!/usr/bin/python3

from atcom import ATCom

at = ATCom()

# 1
try:
    response = at.send_at_comm("AT\r\n","OK", ["ERROR", "CME ERROR"])
except RuntimeError:
    print("Runtime Error")
except TimeoutError:
    print("Timeout Error")
else:
    print(response)

# 2
try:
    response = at.send_at_comm("ATI\r\n","OK", ["ERROR", "CME ERROR"])
except RuntimeError:
    print("Runtime Error")
except TimeoutError:
    print("Timeout Error")
else:
    print(response)

# 3
try:
    response = at.send_at_comm("ATV1\r\n","OK", ["ERROR", "CME ERROR"])
except RuntimeError:
    print("Runtime Error")
except TimeoutError:
    print("Timeout Error")
else:
    print(response)

# 4
try:
    response = at.send_at_comm("ATE1\r\n","OK", ["ERROR", "CME ERROR"])
except RuntimeError:
    print("Runtime Error")
except TimeoutError:
    print("Timeout Error")
else:
    print(response)

# 5
try:
    response = at.send_at_comm("AT+CMEE=2\r\n","OK", ["ERROR", "CME ERROR"])
except RuntimeError:
    print("Runtime Error")
except TimeoutError:
    print("Timeout Error")
else:
    print(response)

# 6
try:
    response = at.send_at_comm("AT+IPR?\r\n","OK", ["ERROR", "CME ERROR"])
except RuntimeError:
    print("Runtime Error")
except TimeoutError:
    print("Timeout Error")
else:
    print(response)

# 7
try:
    response = at.send_at_comm("AT+GSN\r\n","OK", ["ERROR", "CME ERROR"])
except RuntimeError:
    print("Runtime Error")
except TimeoutError:
    print("Timeout Error")
else:
    print(response)

# 8
try:
    response = at.send_at_comm("AT+QURCCFG=\"urcport\",\"usbat\"\r\n","OK", ["ERROR", "CME ERROR"])
except RuntimeError:
    print("Runtime Error")
except TimeoutError:
    print("Timeout Error")
else:
    print(response)

# 9
try:
    response = at.send_at_comm("AT+CPIN?\r\n","OK", ["ERROR", "CME ERROR"])
except RuntimeError:
    print("Runtime Error")
except TimeoutError:
    print("Timeout Error")
else:
    print(response)

# 10
try:
    response = at.send_at_comm("AT+QCCID\r\n","OK", ["ERROR", "CME ERROR"])
except RuntimeError:
    print("Runtime Error")
except TimeoutError:
    print("Timeout Error")
else:
    print(response)