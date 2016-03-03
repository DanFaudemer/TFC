 # -*- coding: utf-8 -*-

import os,sys
from PyQt4 import QtCore, QtGui, uic
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4 import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

from Engine.Model import Model
from pubsub import pub
from collections import deque
import numpy as np

mainGUI = uic.loadUiType("CarGUI.ui")[0] # load ui
plot2D = uic.loadUiType("Plot2D.ui")[0]

class PlotWidgetClass(QtGui.QWidget, plot2D):
    def __init__(self, parent=None, MainWindow=None ):
        QtGui.QWidget.__init__(self,parent)
        self.setupUi(self)
        self.ntb = NavigationToolbar(self.mpl_w, self.frame_plot)
        self.plot_frame_layout.addWidget(self.ntb)
        self.show()
        self.MainWindow = MainWindow
        
        
        self.colors = ['b','g','r','c','m','y','k']
        self.fig = self.mpl_w.figure
        self.ax=self.fig.add_subplot(111)
        self.ax.hold(True)
        self.lines = []
        self.plotted_list = []
        self.legends=[]
        
        #signals:
        self.btn_plotsel.clicked.connect(self.add_var_to_plot)
        self.btn_clr.clicked.connect(self.clear_plot)
        self.btn_remvar.clicked.connect(self.remove_var_from_plot)
        self.lst_plotvar.itemSelectionChanged.connect(self.sel_changed)
        
        pub.subscribe(self.listener_new_value_received,'var_value_update')
        print('jinit plot')
        
    def closeEvent(self, event):
        for line in self.lines:
            line[0].clear()
            line[1].clear()
        self.lines.clear()
        for id in self.plotted_list: #stop var if not selected in main windows
            if id != self.MainWindow.selected_var_id:
                pub.sendMessage('stop_using_var',varid=id)
        self.MainWindow.listPlot.remove(self)
        event.accept()
    
    def event(self,event):
        if(event.type()==QtCore.QEvent.KeyPress) and (event.key()==QtCore.Qt.Key_Return):
            self.MainWindow.btn_stop.click()
            return True
        return QtGui.QWidget.event(self,event)
        
    def add_var_to_plot(self):
        print("j'add var to plot")
        cur_id = self.MainWindow.selected_var_id
        if not cur_id:
            print("no id to plot")
            return
        if cur_id in self.plotted_list:
            return
        
        # new var start à l'index des var (offset sur les x)
        
        pub.sendMessage('using_var',varid=cur_id)
        self.plotted_list.append(cur_id)
        self.lst_plotvar.addItem(self.MainWindow.variables[cur_id]['name'])
        self.lines.append((deque(maxlen=10000),deque(maxlen=10000)))
        self.legends.append(self.MainWindow.variables[cur_id]['name'])
        self.ax.legend(self.legends)
        
    def listener_new_value_received(self, varid, data):
        print("hop a new value")
        if not varid in self.plotted_list:
            return
        else:
            index = self.plotted_list.index(varid)
            
        if len(data['values']) == 1:
            self.lines[index][1].append(data['values'][0])
            self.lines[index][0].append(len(self.lines[index][0]))
        else:
            self.lines[index][0].clear()
            self.lines[index][1].clear()
            self.lines[index][0].extend(np.arange(len(data['values'])))
            self.lines[index][1].extend(data['values'])
            
        i=0
        self.ax.cla()
        for line in self.lines:
            self.ax.plot(line[0], line[1],self.colors[i],antialiased=True)
            i+=1
        # rduire fréq affichage (trouver une new méthode d'affichage? 
        print("end")
        self.mpl_w.axes.set_autoscale_on(True)            
        self.mpl_w.draw()
        
        if(self.lst_plotvar.currentItem().text() == data['name']):
            self.lbl_valuesel.setText(str(data['values' ][0]))
    
    def remove_var_from_plot(self):
        for key in self.MainWindow.variables:
            if self.lst_plotvar.currentItem().text() == self.MainWindow.variables[key]:
                
                if self.MainWindow.variables[key]['ID'] != self.MainWindow.selected_var_id: #if not selected in main window
                    pub.sendMessage('stop_using_var',varid=self.MainWindow.variables[key]['ID'])
                index = self.plotted_list.index(self.MainWindow.variables[key]['ID'])
                self.plotted_list.remove(self.MainWindow.variables[key]['ID'])
                self.lines.remove(self.lines[index])
                self.legends.remove(self.MainWindow.variables[key]['name'])
                self.ax.legend(self.legends)
            #print(self.MainWindow.variables[id])

    def clear_plot(self):
        for line in self.lines:
            line[0].clear()
            line[1].clear()
        self.ax.cla()
        self.mpl_w.draw()
           
        
    def sel_changed(self):
        self.lbl_varsel.setText(self.lst_plotvar.currentItem().text())
        
#**************************************************************#
#*                  MAIN WINDOW                               *#
#**************************************************************# 
class MyWindowClass(QtGui.QMainWindow, mainGUI):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self,parent)
        self.setupUi(self)
        self.listPlot = []
        self.varliste.setColumnWidth(1,  140);
        
        #engine: 
        self.model = Model()
        self.model.start()
        self.refresh_COM_Ports()
        
        #var:
        self.connected = False        
        self.variables = dict()
        self.selected_var_id = None
       # self.listPorts=[]
       # self.listPorts_desc=[]
        
        #signals:
        self.debug.clicked.connect(self.f_debug)
        self.btn_plot.clicked.connect(self.fct_plot)
        self.btn_refresh.clicked.connect(self.refresh_COM_Ports)
        self.btn_connect.clicked.connect(self.start_COM)
        self.btn_disconnect.clicked.connect(self.model.disconnect_com)
        
        self.btn_activate.clicked.connect(self.activate_log)
        self.btn_write.clicked.connect(self.write_value)
        self.varliste.itemSelectionChanged.connect(self.variable_selected)
        
        self.btn_stop.clicked.connect(self.stop_car)
        
        #Subscriptions
        pub.subscribe(self.com_connected,'com_port_connected')
        pub.subscribe(self.com_disconnected,'com_port_disconnected')
        pub.subscribe(self.listener_value_received,'var_value_update')
        pub.subscribe(self.listener_table_received,'logtable_update')
        
    def closeEvent(self, event):
        self.listPlot.clear()
        self.model.stop()
        event.accept()

        
    # FUNCTIONS :     
    def fct_plot(self):
        print('je plot')
        self.listPlot.append(PlotWidgetClass(MainWindow=self))
        self.listPlot[len(self.listPlot)-1].add_var_to_plot()
        
        
    # ------------- COM FRAME -----------------    
    def refresh_COM_Ports(self):
        Ports = self.model.get_ports()
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
        self.model.connect_com(port)
        
    def com_connected(self,port):
        self.connected=True
        self.text_connected.setText("<font color='green'>CONNECTED</font>")
    
    def com_disconnected(self):
        self.connected=False
        self.text_connected.setText("<font color='red'>NO CONNECT</font>")
        self.activate_log()
    #---------------------------------------------

    
    # ------------- LOGGER FRAME -----------------  
    def activate_log(self):
        self.txt_active.setText("<font color='orange'>NO WAITING TABLE</font>")
        self.model.start_controller()
        
        
    def listener_table_received(self, varlist):
        self.variables = varlist
        self.txt_active.setText("<font color='green'>ACTIVE</font>")
        self.varliste.clearContents() #empty table
        self.varliste.setRowCount(0)
       
       #fill table with new values:       
        for key in self.variables:
            row=self.varliste.rowCount()
            self.varliste.insertRow(row)
            self.varliste.setItem(row,0,QtGui.QTableWidgetItem(str(key)))
            self.varliste.item(row,0).setTextAlignment(QtCore.Qt.AlignCenter)            
            self.varliste.setItem(row,1,QtGui.QTableWidgetItem(self.variables[key]['name'])) 
            self.varliste.item(row,1).setTextAlignment(QtCore.Qt.AlignCenter)
            self.varliste.setItem(row,2,QtGui.QTableWidgetItem(str(self.variables[key]['datatype'])))
            self.varliste.item(row,2).setTextAlignment(QtCore.Qt.AlignCenter)
            self.varliste.setItem(row,3,QtGui.QTableWidgetItem(str(self.variables[key]['octets'])))
            self.varliste.item(row,3).setTextAlignment(QtCore.Qt.AlignCenter)
            self.varliste.setItem(row,4,QtGui.QTableWidgetItem())
            self.varliste.item(row,4).setTextAlignment(QtCore.Qt.AlignCenter)
        

    def listener_value_received(self, varid, data):
        if self.selected_var_id is None:
            return
        if not self.selected_var_id == varid:
            return
        
        if len(data['values'])==1:
            self.varliste.item(self.varliste.currentRow(),4).setText(str(data['values'][0]))
            #item = QtGui.QTableWidgetItem(data['values'][0])
            #self.varliste.setItem(self.varliste.currentRow(),3,item)
        
        if not self.defined_first:
            self.spb_selvar.setValue(round(data['values'][0],4))        
            self.defined_first = True
            
            
    def write_value(self):
        sel_id_item = self.varliste.item(self.varliste.currentRow(),0)
        if not int(sel_id_item.text()) in self.variables:
            print("Logger_Frame error : ID not found :",sel_id_item.text())
            return
        self.model.write_var(int(sel_id_item.text()),self.spb_selvar.value())
        self.defined_first = False 
        
        
    def variable_selected(self):
        self.list_sel_item = self.varliste.selectedItems()
        try:
            var_id = int(self.list_sel_item[0].text())
        except:
            return
        if not var_id in self.variables:
            print("Logger_Frame error : ID not found :",var_id)
            return
        
        self.defined_first = False    
        # Tell Variable manager we are stopped with former var
        # and we need the new one
        pub.sendMessage('stop_using_var',varid=self.selected_var_id)
        pub.sendMessage('using_var',varid=var_id)
        self.selected_var_id = var_id
        
        # If selected variable is writeable
        if self.variables[var_id]['writeable']:
            self.lbl_selvar.setText(self.variables[var_id]['name'])                      
        else:
            self.lbl_selvar.setText("** Variable not writeable **")

    #---------------------------------------------        
    
    # ------------- CONTROL FRAME -----------------  
    def stop_car(self):
        self.model.write_var(0,self.btn_stop.isChecked())
    
    #---------------------------------------------
    def f_debug(self):
        # row=self.varliste.rowCount()
        # self.varliste.insertRow(row)
        # self.varliste.setItem(row,0,QtGui.QTableWidgetItem(str(99))) 
        # self.varliste.item(row,0).setTextAlignment(QtCore.Qt.AlignCenter)
        # self.varliste.setItem(row,1,QtGui.QTableWidgetItem("bonjourtoicommentçava"))
        # self.varliste.item(row,1).setTextAlignment(QtCore.Qt.AlignCenter)
        # self.varliste.setItem(row,2,QtGui.QTableWidgetItem("2"))
        # self.varliste.item(row,2).setTextAlignment(QtCore.Qt.AlignCenter)
        # self.varliste.setItem(row,3,QtGui.QTableWidgetItem())
        # self.varliste.item(row,3).setTextAlignment(QtCore.Qt.AlignCenter)
        # self.varliste.setItem(row,4,QtGui.QTableWidgetItem("3"))  
        # self.varliste.item(row,4).setTextAlignment(QtCore.Qt.AlignCenter)
        # print(self.varliste.item(row,1).sizeHint())
        self.selected_var_id=1
        
        self.variables={1:{'ID':1,'name':'bonjour','Value':125}}
        
        
# création fenetre/class 
if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    myWindow = MyWindowClass(None)
    myWindow.show()
    app.exec_()
    #sys.exit(app.exec_())