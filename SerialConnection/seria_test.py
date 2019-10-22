from tkinter import *
import tkinter as tk
import serial
import cv2
import time


class GUI:
    def __init__(self,root):

        self.setPnt = tk.Label(root, text="Set point ")
        self.setPnt.pack(side=LEFT)

        self.spinBoxZ = tk.Spinbox(root, from_ =-24, to=24,textvariable = var ,command = self.printValues)
        self.spinBoxZ.pack(side=LEFT)

        self.setBtn = tk.Button(root, text = "Set", command = self.printValues)
        self.setBtn.pack(side=LEFT)

        self.setConn = tk.Button(root, text = "Connect", command = self.ArduinoConnection)
        self.setConn.pack(side=LEFT)

#        self.setBtn1 = tk.Button(root, text = "Close", command = root.quit)
#        self.setBtn1.pack()

    def printValues(self):
        print("Written: {}".format(self.spinBoxZ.get()))
#        try:
        serPC.read(size=100)
#        serialcmd = input(self.spinBoxZ.get())
        serPC.write('0'.encode())
        print("Connection established")
#        except:
#        print("Connection failed ...")

    def ArduinoConnection(self):
            global serPC
            print("Establishing serial connection between Computer and Arduino ...")
            try:
                serPC = serial.Serial('COM10',9600,timeout =0,parity = serial.PARITY_EVEN,rtscts=1)
                print("Connection established!")
                return serPC
            except:
                print("Connection to Arduino failed")


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