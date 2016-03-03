#import serial
import sys
import threading 



#Serial
ser = serial.Serial(9, baudrate=115200)  # open first serial port
print ser.portstr       # check which port was really used
global channel1
global channel2
channel1=[0]*128
channel2=[0]*128

#Graph
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
import time
#plt.ion()
x = range(0,128)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_ylim([0,5000])
line1, = ax.plot(x, channel1) # Returns a tuple of line objects, thus the comma
line2, = ax.plot(x, channel2) # Returns a tuple of line objects, thus the comma

def init():
    line2.set_ydata(range(0,128))
    fig.canvas.draw()
    #print ("hello")
    return line2,

def animate(i):
    line1.set_xdata(x)
    line1.set_ydata(channel1)
    line2.set_ydata(channel2)
    fig.canvas.draw()
    #print ("hello")
    return line1,line2,

def UART(nb, stop_event):
#    reposne=""
    while (1):#not stop_event.is_set()) :
        response = ser.readline().replace("L:","")
        response = response.split(',')
        #print (response)
        if ( len(response) == 256) :
            for i in range(0, 127):
                channel1[i] = int(response[i],16)
            for i in range(128, 255):
                channel2[i-128] = int(response[i],16)
            #print (channel2)
        #sys.stdout.write(response)
        #print(max(channel2))
        #print ("-------------------")

        
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=20, blit=True)
uart_stop= threading.Event()
uart = threading.Thread(None, UART, None, args=(1,uart_stop))
uart.start()
plt.show()
#uart_stop.set()

