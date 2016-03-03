# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 20:18:48 2014

@author: jerome
"""

from CarGUI import *
from CarUART import *
import sys, os 
import threading 

from time import sleep

global reset_status
reset_status=False

from camReadGUI import *


def readUART():
	global reset_status
	logFile = open("logPython.txt", "w")
	sleep(2)
	while(1):
		if not reset_status:
                 
                 value = str(uart.readUART())
                 cam.update(value)                 
    
                 gui.writePS( "<< " +str(value), "receive")
                 #print  value
                 logFile.write(str(value))
                 logFile.flush()
                 #sleep(0.001) #Slow speed display for avoid crash
			#print(uart.readUART())
		else:
			sleep(0.25) # Time in seconds.
		
def sendUART(*j):
	#print gui.sendPS()
	uart.writeUART(gui.sendPS())

def sendConf(*j):
    string = uart.createPID_POS(gui.Ppspbx.get(),gui.Ipspbx.get(), gui.Dpspbx.get())
    string += uart.createPID_SPE(gui.Pvspbx.get(), gui.Ivspbx.get(), gui.Dvspbx.get(), gui.offset_vit.get(), gui.vit_max.get())
    string += uart.createPID_DIFF(gui.Pdspbx.get(), gui.Idspbx.get(), gui.Ddspbx.get())   
    string += uart.createCam(gui.seuil.get())
    uart.writeUART(string)
    string = string[:-2] #Remove the last \n
    string = string.replace("\n", "\n>> ")
    gui.writePS(">> "+string +"\n", "send")
    

def reset(*j):
	global reset_status
	reset_status=True
	gui.resetPS()
	status = uart.resetUART()
	if status == 'fail':
		gui.writePS("Fail Open Port!\n")
	else:
		reset_status=False
  
def showLine(*j):
    cam.display()
		
cam = CamRead()  
gui = GUI(None)		
uart = UART(Port="COM3", baudrate=115200)
threadUART = threading.Thread(target=readUART)
threadUART.start()

# event : 
gui.bouton_sendPS.bind
gui.entryPS.bind("<Return>", sendUART)
gui.bouton_rstPS.bind("<Button-1>", reset)

gui.button_line.bind("<Button-1>", showLine)

gui.bouton_sendConf.bind("<Button-1>", sendConf)



gui.mainloop()

uart.closeUART()