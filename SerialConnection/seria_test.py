import serial
import time
import keyboard
import cv2


ser = serial.Serial('/dev/ttyUSB1',19200)
s = [0,1]
i = 1
while True:
#    read_serial=ser.readline()
#    s[0] = str(int (ser.readline(),16))
#    print(s[0])
#    print(read_serial)

    print(i)
    ser.write(i)
    i = i+1
    time.sleep(0.1)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("r"):
        quit()