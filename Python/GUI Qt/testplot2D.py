  # -*- coding: utf-8 -*-

import os,sys
from PyQt4 import QtCore, QtGui, uic

import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from collections import deque
import matplotlib.pyplot as plt
import matplotlib.lines as ln

plot2D = uic.loadUiType("Plot2D.ui")[0]

class PlotWidgetClass(QtGui.QWidget, plot2D):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.setupUi(self)
       # self.x=np.arange(0.0,3.0,0.01)
       # self.y = np.cos(2*np.pi*self.x)
       # self.mpl_w.axes.plot(self.x,self.y)
        self.ntb = NavigationToolbar(self.mpl_w, self.frame_plot)
        self.plot_frame_layout.addWidget(self.ntb)
        self.show()
        
        self.colors = ['b','g','r','c','m','y','k']
        self.fig = self.mpl_w.figure
        self.ax=self.fig.add_subplot(111)
        self.ax.hold(True)
        #self.ax.set_autoscale_on(True)
        
        self.lines = []
        self.lines.append( (deque(),deque()))
        self.lines.append( (deque(),deque()))
        self.lines.append( (deque(),deque()))
        self.lines[0][0].append(0)
        self.lines[0][1].append(0)
        print(self.lines)
        #self.mpl_w.axes.add_line(ln.Line2D(self.x[0],self.y[0],color='r'))
        #self.mpl_w.axes.add_line(ln.Line2D(self.x[1],self.y[1],color='g'))
        #self.lines = self.mpl_w.axes.lines
        print(self.mpl_w.axes.lines)
        
        self.i=0

        self.btn_plotsel.clicked.connect(self.listener_new_value_received)
        #self.btn_clr.clicked.connect(self.addit)
        self.btn_clr.clicked.connect(self.clear_plot)
        
    def listener_new_value_received(self):
        lenx0 = len(self.lines[0][0])
        print(len(self.lines[0][0])-1)
        print(self.lines[0][0][len(self.lines[0][0])-1])
        self.lines[0][0].append(self.lines[0][0][len(self.lines[0][0])-1] + 0.01)
        self.lines[0][1].append(np.cos(2*np.pi*self.lines[0][0][lenx0]))
        lenx2 = len(self.lines[2][0])
        self.lines[2][0].append(lenx2*0.01)
        self.lines[2][1].append(np.log(self.lines[2][0][lenx2]+1))
        if(self.i%5==0):
            lenx1 = len(self.lines[1][0])
            self.lines[1][0].append(lenx1 * 0.01)
            self.lines[1][1].append(np.cos(2*np.pi*self.lines[1][0][lenx1])*-2)
        self.i+=1
        segx=[]
        segy=[]
        i=0
        #self.ax.cla()
        line=self.lines[0]
        #for line in self.lines:
            #self.ax.plot(line[0], line[1],self.colors[i],antialiased=True)
        if len(self.lines[0][0])>2:
            segx=[self.lines[0][0].popleft(), self.lines[0][0].popleft()]
            segy=[self.lines[0][1].popleft(), self.lines[0][1].popleft()]
        print(self.lines[0][0])
        print(segx,segy)
        
        tab = np.arange(10)
        print(tab)
        taby=np.cos(2*np.pi*tab/100)
        print(taby)
        self.ax.plot(tab[1:5], taby[1:5],self.colors[i],antialiased=True)
        i+=1

       # self.ax.legend(["allo","bpnj","enrk"])
        self.mpl_w.axes.set_autoscale_on(True) #axis: [‘x’ | ‘y’ | ‘both’]
        self.mpl_w.draw()
        
        
        
 ###
# '-' 	solid line style
# '--' 	dashed line style
# '-.' 	dash-dot line style
# ':' 	dotted line style
# '.' 	point marker
# ',' 	pixel marker

# ‘b’ 	blue
# ‘g’ 	green
# ‘r’ 	red
# ‘c’ 	cyan
# ‘m’ 	magenta
# ‘y’ 	yellow
# ‘k’ 	black
# ‘w’ 	white
    def clear_plot(self):
        for line in self.lines:
            line[0].clear()
            line[1].clear()
        self.ax.cla()
        self.mpl_w.draw()
        
        
    def addit(self):
        self.lst_plotvar.addItem('allo')
        
        # création fenetre/class 
if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    myWindow = PlotWidgetClass(None)
    myWindow.show()
    app.exec_()
    #sys.exit(app.exec_())