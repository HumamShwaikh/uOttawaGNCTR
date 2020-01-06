##############
# Script listens to seral port and writes contents into a file
##############
# requires pySerial to be installed
import serial
from serial import Serial
import keyboard  # using module keyboard
import datetime

now = datetime.datetime.now()
serial_port = 'com4'
baud_rate = 9600  # In arduino, Serial.begin(baud_rate)
write_to_file_path = "data" + str(now.year) + str(now.month) + str(now.day) + str(now.hour) + str(now.minute) + ".txt"

output_file = open(write_to_file_path, "w+")
ser = serial.Serial(serial_port, baud_rate)
while (keyboard.is_pressed('q') == False):
    line = ser.readline()
    # ser.readline returns a binary, convert to string
    line = line.decode("utf-8")
    print(line)
    output_file.write(line)
