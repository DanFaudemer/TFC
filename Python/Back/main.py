from PyQt4 import QtCore, QtGui, uic
import sys
from Engine.SerialPort import SerialPort
mainGUI = uic.loadUiType("CarGUI.ui")[0] # load ui Copyright Jérome Mallet 2015
 
class MyWindowClass(QtGui.QMainWindow, mainGUI):
	def __init__(self, parent=None):
	
		self.lap = 0
		QtGui.QMainWindow.__init__(self,parent)
		self.setupUi(self)
		self.listPlot = []
		self.lapTable.setColumnWidth(1,  140);
		self.lapTable.setRowCount(0)
        #engine: 
		self.serialthread = SerialPort()	
		self.serialthread.start()
		self.refresh_COM_Ports()
        
        #var:
		self.connected = False        
		self.variables = dict()
		self.selected_var_id = None
       # self.listPorts=[]
       # self.listPorts_desc=[]
        
        #signals:
		
		self.btn_refresh.clicked.connect(self.refresh_COM_Ports)
		self.btn_connect.clicked.connect(self.start_COM)
		self.btn_disconnect.clicked.connect(self.serialthread.disconnect)
		
		#Connexion :
		
		
		self.connect( self.serialthread, QtCore.SIGNAL("com_connected(QString)"), self.com_connected )
		self.connect( self.serialthread, QtCore.SIGNAL("refresh_results(QString)"), self.refresh_results )
		
	def refresh_results(self, readline) :
		readline = str(int(int(readline)/1000)) +" s " + str(int(readline)%1000) + " ms"
		row=self.lapTable.rowCount()
		self.lapTable.insertRow(row)
		self.lapTable.setItem(row,0,QtGui.QTableWidgetItem(str(row)))
		self.lapTable.item(row,0).setTextAlignment(QtCore.Qt.AlignCenter)
		
		self.lapTable.setItem(row,1,QtGui.QTableWidgetItem(readline)) 
		self.lapTable.item(row,1).setTextAlignment(QtCore.Qt.AlignCenter)
		
		
	
	def closeEvent(self, event):
		self.listPlot.clear()
		self.serialthread.stop()
		event.accept()

        
        
    # ------------- COM FRAME -----------------    
	def refresh_COM_Ports(self):
		Ports = self.serialthread.get_ports()
		self.listPorts=[]
		self.listPorts_desc=[]
		print('COM ports list :') 
		for p, desc, hwid in sorted(Ports):
			print('--- %s %s %s\n' % (p, desc, hwid))
			self.listPorts.append(p)
			self.listPorts_desc.append(desc)
		self.comboBox.clear()
		self.comboBox.addItems(self.listPorts_desc)
    
	def start_COM(self):
		if self.connected:
			return
        
		self.text_connected.setText("<font color='orange'>CONNECTING</font>")
		if self.comboBox.currentText()=="":
			print("No port selected, aborting.")
			self.text_connected.setText("<font color='red'>NO CONNECT</font>")
			return
        
		port=self.listPorts[self.comboBox.currentIndex()]
		self.serialthread.connect(port,115200)
	def com_connected(self,text):
		self.connected=True
		self.text_connected.setText("<font color='green'>CONNECTED</font>")
    
	def com_disconnected(self):
		self.connected=False
		self.serialthread.disconnect()
		self.text_connected.setText("<font color='red'>NO CONNECT</font>")
		self.activate_log()
    #---------------------------------------------
	
	


	
# création fenetre/class 
if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    myWindow = MyWindowClass(None)
    myWindow.show()
    app.exec_()