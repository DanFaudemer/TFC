# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 20:18:48 2014

@author: jerome
"""

import serial
import sys
import threading 
#from CarGUI import *

class UART:
	
	def __init__(self, Port, baudrate=19200):
		#Serial
		self.stringUART=""
		#self.read=False
		self.ser = serial.Serial(Port, baudrate)  # open first serial port /dev/ttyACM0
		print 'Port: '+self.ser.name       # check which port was really used
		#self.thread = threading.Thread(target=self.getUARTdata)
		#self.thread.start()
		
	def getUARTdata(self, *j):
		while(1):
			#print(self.ser.readline())
			if self.read==True:
					self.stringUART=""
					self.read=False
			else:
					self.stringUART = self.stringUART+self.ser.readline()
			
		
	def readUART(self, *j):
		#temp = self.stringUART
		#self.read=True
		return self.ser.readline()
		
	def writeUART(self, string, *j):
		self.ser.write(string)
		
	def closeUART(self, *j):
		if self.ser.isOpen():
			self.ser.close()
			
	def resetUART(self,*j):
		if self.ser.isOpen():
			self.ser.close()
		while self.ser.isOpen()==True:
			pass
		try: 
			self.ser.open()
		except:
			return 'fail'
   
	def createPID_POS(self, POS_P, POS_I, POS_D):
         string = "";
         string = "DIR_P:"+POS_P+";\n\r"
         string += "DIR_I:"+POS_I+";\n\r"
         string += "DIR_D:"+POS_D+";\n\r"
         return string;
         
	def createPID_SPE(self, SPE_P, SPE_I, SPE_D, SPE_min = "0.0", SPE_max="1.0"):
         string = "SPE_P:"+SPE_P+";\n\r"
         string += "SPE_I:"+SPE_I+";\n\r"
         string += "SPE_D:"+SPE_D+";\n\r"
         string += "SPE_MIN:"+SPE_min+";\n\r"
         string += "SPE_MAX:"+SPE_max+";\n\r"
         
         return string;
	def createPID_DIFF(self, DIFF_P, DIFF_I, DIFF_D):
         string = "DIFF_P:"+DIFF_P+";\n\r"
         string += "DIFF_I:"+DIFF_I+";\n\r"
         string += "DIFF_D:"+DIFF_D+";\n\r"
         
         return string;         

	def createCam(self, seuil):
         string = "CAM_SEUIL:"+seuil+";\n\r"
         return string
		
if __name__=="__main__":
    uart1 = UART(Port="COM11", baudrate=115200)
    