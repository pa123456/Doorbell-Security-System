import serial
import os
import time
from subprocess import call

ser = serial.Serial('/dev/cu.usbmodem1411', 9600)

print("Waiting for data...")

while True:
    data = ser.readline()[:-1]

    if data == "busy":
        # Someone is at the door
        print("Someone is at the door")

        #open facetime
        call(["osascript", "./FaceTimeCall.scpt"])

    elif data == "available":
        # Nobody is at the door
        print("Nobody is at the door")


