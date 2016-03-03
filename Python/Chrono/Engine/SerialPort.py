# Copyright (C) 2014 Rémi Bèges
# For conditions of distribution and use, see copyright notice in the LICENSE file

from PyQt4 import QtCore, QtGui
import serial
from queue import Queue
from serial.tools.list_ports import comports

from PyQt4.QtCore import QThread

#Serial data processing class
class SerialPort(QThread):

	def __init__(self):
		QtCore.QThread.__init__(self)
		self.ser = serial.Serial()
		self.ser.timeout = 1
		self.force = False
		self.default_to = False
		self.rxqueue = Queue(0)
		self.running = True;
		self.processed_octets = 0
		self.maxinwaiting = 0

	def connect(self,port,baudrate,force=False,default_to=False):
		self.ser.baudrate = baudrate
		self.ser.port = port
		self.force =force
		self.default_to = force
		
		portlist = self.get_ports()
		port_found = -1
		port_amount = 0
		terminate = False

		#List all COM ports      
		for p, desc, hwid in sorted(portlist):
			port_amount+=1
			if p == self.ser.port:
				port_found = 1
				
		#In case no port is found 
		if port_amount == 0:
			print('No COM port found.')
			print('   - can use \'force\' mode to try connect anyway.')
			terminate = True
			
			if self.force:
				  terminate = False
				  
		#In case ports are found but not chosen one
		if port_amount > 0 and port_found == -1:
			print(port,' port not found.')
			print('   - can use \'default\' mode to default to fall back to a valid port.')
			terminate = True
			
			if self.default_to:
				terminate = False
				ser.port = [x[1] for x in portlist][0]
				
		#Exit prematurely if error
		if terminate:
			print(port, 'port non valid, aborting.')
			return False
		
		try:
			self.ser.open()
		except:
			print("Serial port : Port ",port," found but impossible to open. Try to physically disconnect.")
			self.emit( QtCore.SIGNAL('com_disconnected(QString)'), "nok" )
			self.ser.close()
			return False

		if self.ser.isOpen():
			print('Connected to port ',self.ser.port)
			self.emit( QtCore.SIGNAL('com_connected(QString)'), "ok" )
			
			return True

		print("Unknow serial connection error, aborting")
		
	def get_ports(self):
		return serial.tools.list_ports.comports()
		
	def stop(self):
		self.running = False;

	def write(self, frame):
		if self.ser.isOpen() and self.running:
			return self.ser.write(frame)

	def disconnect(self):
		self.emit( QtCore.SIGNAL('com_disconnected(QString)'), "nok" )
		if self.ser.isOpen():
			self.ser.close()
			
		


	def run(self):
		#Main serial loop  
		received = 0	
		while self.running:
			if self.ser.isOpen():
				try:
					#self.emit( QtCore.SIGNAL('refresh_results(QString)'), "123")
					readLine = self.ser.readline().decode("utf-8")
					readLine = readLine.replace("\r", "")
					readLine = readLine.replace("\n", "")					
					if(readLine.isdigit()) : 
						received = 1 
		
					
				except:
					pass
			if(received):
				self.emit( QtCore.SIGNAL('refresh_results(QString)'), readLine)
				received = 0
				
		self.ser.close()
		print("Serial thread stopped.")
		
		
