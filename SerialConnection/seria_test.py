from tkinter import *
import tkinter as tk
import serial
import cv2
import time

value1 = 0

def sendValues(selected):
    if selected == 0:
        print("Data written: 0")

#            serPC.write('0')

    elif selected == 1:
#            serPC.write('1')
        print("Data written: 1")




class GUI:
    def __init__(self,root,*args, **kwargs):

        self.setPnt = tk.Label(root, text="Set point ")
        self.setPnt.pack(side=LEFT)

        self.spinBoxZ = tk.Spinbox(root, from_ =-24, to=24,textvariable = var ,command = self.printValues)
        self.spinBoxZ.pack(side=LEFT)

        self.setBtn = tk.Button(root, text = "Set", command = self.printValues)
        self.setBtn.pack(side=LEFT)

        self.setConn = tk.Button(root, text = "Connect", command = self.ArduinoConnection)
        self.setConn.pack(side=LEFT)

        self.setBtnUp = tk.Button(root, text = "Up", command = self.btnUp)
        self.setBtnUp.pack()

        self.setBtnDown = tk.Button(root, text = "Down", command = self.btnDown)
        self.setBtnDown.pack()

#        self.setBtn1 = tk.Button(root, text = "Close", command = root.quit)
#        self.setBtn1.pack()

    def btnUp(self):
        print("Data written: 1")
        serPC.write('1'.encode())

    def btnDown(self):
        print("Data written: 0")
        serPC.write('0'.encode())


    def printValues(self):

#        global value1
#        changeValue(self)

#        while 1:
#            inputData = input()
#            print("You entered: ", inputData)
#        print("Written: {}".format(self.spinBoxZ.get()))
        print(self.spinBoxZ.get())
#        value1 = int(self.spinBoxZ.get())
#        try:
#            serPC.read(size=100)
#        serialcmd = input(self.spinBoxZ.get())
        if int(self.spinBoxZ.get()) >= int(value1):
            print("Data written: 1")

#            serPC.write('0')
#            print("Data written: 0")

        elif int(self.spinBoxZ.get())-int(value1) < int(value1):
#            serPC.write('1')
            print("Data written: 0")

#        value1 = int(self.spinBoxZ.get())

    def ArduinoConnection(self):
            global serPC
            print("Establishing serial connection between Computer and Arduino ...")
            try:
                serPC = serial.Serial('/dev/ttyACM0',115200,timeout =0,parity = serial.PARITY_EVEN,rtscts=1)
                print("Connection established!")
                return serPC
            except:
                print("Connection to Arduino failed")


def changeValue(self):
    global selected
    selected = format(self.spinBoxZ.get())
    sendValues(selected)
    print("selected is assigned ...")
#    return selected

#def printSelected(selected):
#if selected == 0:
#    print("selected 0")
#
#elif selected == 1:
#    print("selected 1")

root = tk.Tk()
var = tk.StringVar(root)
var.set("0")
var1 = tk.StringVar()
var2 = tk.StringVar()
root.title("Z Position")
root.geometry('500x100')
var1.set(0)
var2.set(0)


guiOpen = GUI(root)

root.mainloop()