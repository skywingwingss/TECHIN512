import csv
import os
import sys
import serial
import serial.tools.list_ports as list_ports
import Reading
from datetime import datetime


serialPort = []
usingPorts = list(list_ports.comports())
nrf=[]
for port in usingPorts:
    #debug to detect Serial name
    print(port.description)
    if sys.platform.startswith('win'):
        if ("Serial" in port.description) or ("串行" in port.description):
            serialPort.append(port.device)
            nrf.append(Reading.NRF5284(port.device))
        # end
    elif sys.platform.startswith('darwin'):
        if "Sense" in port.description:
            serialPort.append(port.device)
            nrf.append(Reading.NRF5284(port.device))


print("1",nrf[0].get_light())
print("2",nrf[1].get_light())
