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
from mpl_toolkits.mplot3d import Axes3D

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
        self.ax=self.fig.gca(projection='3d')
        self.ax.hold(True)
        self.y=0
        #self.ax.set_autoscale_on(True)
        
        self.lines = []
        self.lines.append( (deque(),deque()))
        self.lines.append( (deque(),deque()))
        self.lines.append( (deque(),deque()))
        print(self.lines)
        #self.mpl_w.axes.add_line(ln.Line2D(self.x[0],self.y[0],color='r'))
        #self.mpl_w.axes.add_line(ln.Line2D(self.x[1],self.y[1],color='g'))
        #self.lines = self.mpl_w.axes.lines
        print(self.mpl_w.axes.lines)
        
        self.i=0

        self.btn_plotsel.clicked.connect(self.listener_new_value_received)
        self.btn_clr.clicked.connect(self.addit)
        
        self.cam=np.ones(128)
        self.cam[0:60]*=0
        self.cam[80:]*=0

        
    def listener_new_value_received(self):
        x=np.arange(128)
        y=np.ones(128)*self.y
        self.ax.plot(x,y,self.cam,self.colors[0],antialiased=True)

        self.y+=0.1
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


    def addit(self):
        self.lst_plotvar.addItem('allo')
        
        # création fenetre/class 
if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    myWindow = PlotWidgetClass(None)
    myWindow.show()
    app.exec_()
    #sys.exit(app.exec_())