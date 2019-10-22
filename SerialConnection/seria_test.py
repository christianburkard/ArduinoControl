import serial
import time
import keyboard
import cv2
import smbus
import time
import os
#
ser = serial.Serial('/dev/ttyUSB1',19200,timeout =0,parity = serial.PARITY_EVEN,rtscts=1)
ser.read(size=100)
s = [0,1]
i = 1
while True:
#    read_serial=ser.readline()
#    s[0] = str(int (ser.readline(),16))
#    print(s[0])
#    print(read_serial)
    k = bin(i)
    print(k)
    ser.write(b'H')
    i = i+1
    time.sleep(0.5)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("r"):
        quit()

#have to run 'sudo apt-get install python-smbus'

#
## display system info
#print(os.uname())
#
#bus = smbus.SMBus(1)
#
## I2C address of Arduino Slave
#i2c_address = 0x07
#i2c_cmd = 0x01
#
#def ConvertStringToBytes(src):
#    converted = []
#    for b in src:
#        converted.append(ord(b))
#    return converted
#
## send welcome message at start-up
#bytesToSend = ConvertStringToBytes("Hello Uno")
#bus.write_i2c_block_data(i2c_address, i2c_cmd, bytesToSend)
#
## loop to send message
#exit = False
#while not exit:
#    r = raw_input('Enter something, "q" to quit"')
#    print(r)
#
#    bytesToSend = ConvertStringToBytes(r)
#    bus.write_i2c_block_data(i2c_address, i2c_cmd, bytesToSend)
#
#    if r=='q':
#        exit=True
