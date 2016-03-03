# -*- coding: utf-8 -*-
"""
Created on Wed Jul 30 16:28:27 2014

@author: B48861
"""

import serial
import sys
import threading 

import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
import time


class CamRead:    	 
    
    #Serial
    def __init__(self):
        self.LIMITMIN = 20
        self.LIMITMAX = 118 
        self.channel1=[0]*128
        self.channel2=[0]*128
        self.derivate_chan1 = [0]*128
        self.derivate2_chan1 = [0]*128
        self.LIMITMIN = 20
        self.LIMITMAX = 118 
        self.SEUIL_DETECTION = 50
        self.limit = [0]*128
        self.posLine1 = 0 #(LIMITMAX-LIMITMIN)/2
        self.index_debut_l=0
        #Graph
        
        #plt.ion()
        
        self.init_plot()
        
    def init_plot(self):
        self.x = range(0,128)
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        self.ax.set_ylim([0,5000])
        self.line1, = self.ax.plot(self.x, self.channel1) # Returns a tuple of line objects, thus the comma
        self.line2, = self.ax.plot(self.x, self.channel2) # Returns a tuple of line objects, thus the comma
        self.deriv_line1, = self.ax.plot(self.x, self.derivate_chan1) # Returns a tuple of line objects, thus the comma
        self.deriv_line1.set_color('red')
        self.deriv2_line1, = self.ax.plot(self.x, self.derivate2_chan1) # Returns a tuple of line objects, thus the comma
        self.deriv2_line1.set_color('blue')
        self.posLine_line1, = self.ax.plot(self.x, [0]*128) 
        
        for i in range (0, self.LIMITMIN) :
            self.limit[i] = 0
        
        for i in range (self.LIMITMIN, self.LIMITMAX) :
            self.limit[i] = 4095
        
        for i in range (self.LIMITMAX, 128) :
            self.limit[i] = 0
        
        self.limit_plot = self.ax.plot(self.x, self.limit) 
        
        
        self.anim = animation.FuncAnimation(self.fig, self.animate, init_func=self.init,
        		   frames=200, interval=500, blit=True)
        
        #self.fig.show()
        
        
    	
    def init(self):
        self.line2.set_ydata(range(0,128))
        self.fig.canvas.draw()
        #plt.close("all") # Not display the line at start up
        return self.line2,

    def animate(self,i):

        
        self.line1.set_xdata(self.x)
        self.line1.set_ydata(self.channel1)
        self.line2.set_ydata(self.channel2)
        self.deriv_line1.set_ydata(self.derivate_chan1)
        self.deriv2_line1.set_ydata(self.derivate2_chan1)
    
        self.data = [80]*128
        self.data[self.posLine1] = 4096
        #print("Posline : ")
       # print(posLine1)
        self.posLine_line1.set_ydata(self.data)
        self.fig.canvas.draw()
        return self.line1,self.line2,
        
    
    def display(self):
        self.init_plot()
        self.fig.show()
    def update(self, uart_line):
        #print("test")
        response=uart_line
        response = response.split(',')
        #print(len(response))
        for i in response:
            if(i.find("posLine") >= 0):
                #print(i)
				#interface.termtxt.insert(END, "Port serie non connecte!")
                i = i.replace("posLine : ","")
                try:
                    self.posLine1 = int(i)
                except:
                    break
            elif(i.find("L:") < 0): # si il y a pas "L:"
                #print(i)
                continue
            else:
                response.remove(response[0])
                #print(len(response))
                if ( len(response) == 129) :
                    for i in range(0, 127):
                        self.channel1[i] = int(response[i],16)
	
                            	    #Calc Derivate
                    for i in range (1,128) :
                        self.derivate_chan1[i] = (self.channel1[i] - self.channel1[i-1])/2
                     
                    for i in range (2,128):
                        self.derivate2_chan1[i] = (self.derivate_chan1[i] - self.derivate_chan1[i-1])/2

                break


if __name__=="__main__":
    cam = CamRead()  

   # ca    
    