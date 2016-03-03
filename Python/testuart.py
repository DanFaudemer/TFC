# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 20:18:48 2014

@author: jerome
"""

import CarUART
from Tkinter import *
import threading
from time import sleep



uart2 = CarUART.UART(Port="COM11", baudrate=115200)


def sendtxt():
	uart2.writeUART(entry.get()+"\n\r")
	print entry.get()
	
def sendloop():
	global loop_en
	print(loop_en)
	loop_en = not loop_en

def loop():
	global loop_en
	while 1:
		sleep(0.25) # Time in seconds.
		if loop_en:
			sendtxt()

def read():
	while 1:
		print uart2.readUART()
			
interface = Tk()

entry = Entry(interface)
entry.grid(row=0,columnspan=2, sticky = 'EW')

bsend = Button(interface, text="send", command = sendtxt)
bsend.grid(row=1, column=0, sticky='ENS')

global loop_en
loop_en = False
bloop = Button(interface, text= "loop", command = sendloop)
bloop.grid(row=1, column = 1, sticky='WNS')

threadloop = threading.Thread(target=loop)
threadloop.start()

threadread = threading.Thread(target=read)
threadread.start()

interface.mainloop()
interface.destroy()