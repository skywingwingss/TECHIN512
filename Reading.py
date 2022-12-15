import csv
import os
import sys
import serial
import serial.tools.list_ports as list_ports

class NRF5284():
    def __init__(self,serialPort,bandRate=115200):
        self.device= serial.Serial(serialPort, bandRate)

    def read_raw(self):
        data = (self.device.readline()).decode("utf-8").splitlines()[0].split(',')
        return data

    def get_light(self):
        data=self.read_raw()
        light=int(data[0])+int(data[1])+int(data[2])+int(data[3])

        return light