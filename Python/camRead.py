import serial
import sys
import threading 




def resetUART():                       
	ser.close()
	ser = serial.Serial(PortSerie, baudrate=115200)  # open first serial port /dev/ttyACM0
	

	#Serial
PortSerie = "COM5"
ser = serial.Serial(PortSerie, baudrate=115200)  # open first serial port /dev/ttyACM0
print ser.portstr       # check which port was really used
global channel1
global channel2
global derivate_chan1
global posLine1
global index_debut_l

channel1=[0]*128
channel2=[0]*128
derivate_chan1 = [0]*128
derivate2_chan1 = [0]*128
LIMITMIN = 20
LIMITMAX = 118 
SEUIL_DETECTION = 50
limit = [0]*128
posLine1 = 0 #(LIMITMAX-LIMITMIN)/2
index_debut_l=0
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
deriv_line1, = ax.plot(x, derivate_chan1) # Returns a tuple of line objects, thus the comma
deriv_line1.set_color('red')
deriv2_line1, = ax.plot(x, derivate2_chan1) # Returns a tuple of line objects, thus the comma
deriv2_line1.set_color('blue')
posLine_line1, = ax.plot(x, [0]*128) 

for i in range (0, LIMITMIN) :
    limit[i] = 0

for i in range (LIMITMIN, LIMITMAX) :
    limit[i] = 4095

for i in range (LIMITMAX, 128) :
    limit[i] = 0

limit_plot = ax.plot(x, limit) 


anim = animation.FuncAnimation(fig, animate, init_func=init,
			   frames=200, interval=20, blit=True)
uart_stop= threading.Event()
uart = threading.Thread(None, UART, None, args=(1,uart_stop))
uart.start()
plt.show()
uart_stop.set()
	
def init():
    line2.set_ydata(range(0,128))
    fig.canvas.draw()
    return line2,
    #eturn 0
def animate(i):
    global posLine1
    global index_debut_l
    
    line1.set_xdata(x)
    line1.set_ydata(channel1)
    line2.set_ydata(channel2)
    deriv_line1.set_ydata(derivate_chan1)
    deriv2_line1.set_ydata(derivate2_chan1)

    data = [80]*128
    data[posLine1] = 4096
    #print("Posline : ")
   # print(posLine1)
    posLine_line1.set_ydata(data)
    fig.canvas.draw()
    return line1,line2,

def UART(nb, stop_event):
    global posLine1
    global index_debut_l
    #print("test")
    response=""
    while (1):#not stop_event.is_set()) :
        response = ser.readline()#.replace("L:","")
        response = response.split(',')
        #print(len(response))
        for i in response:
            if(i.find("posLine") >= 0):
                print(i)
				#interface.termtxt.insert(END, "Port serie non connecte!")
                i = i.replace("posLine : ","")
                try:
                    posLine1 = int(i)
                except:
                    break
            elif(i.find("L:") < 0): # si il y a pas "L:"
                print(i)
            else:
                response.remove(response[0])
                #print(len(response))
                if ( len(response) == 129) :
                    for i in range(0, 127):
                        channel1[i] = int(response[i],16)
	
                            	    #Calc Derivate
                    for i in range (1,128) :
                        derivate_chan1[i] = (channel1[i] - channel1[i-1])/2
                     
                    for i in range (2,128):
                        derivate2_chan1[i] = (derivate_chan1[i] - derivate_chan1[i-1])/2
#
                break
#                    posLineLeft = 0
#                    Line_find=0
#                    detect_pic = 0
#                    debut_l=0
#                    fin_l=0

        #print  (max(derivate2_chan1))
        #print  (min(derivate2_chan1))
#                    for i in range (LIMITMIN+1, LIMITMAX) :
#                        if ( derivate2_chan1[i] <= -SEUIL_DETECTION): # Detection de la pente descende
#                            detect_pic = -1
#                        elif ( derivate2_chan1[i] >= SEUIL_DETECTION): # Pente qui monte 
#                            detect_pic = 1
#                        else:
#                            detect_pic = 0

   
#                    if (detect_pic == -1 and debut_l==0 and fin_l==0):
#                        debut_l = 1
#                        index_debut_l = i
#                    elif (detect_pic == 1 and debut_l ==1 and fin_l==0):                
#                        debut_l = 0
#                        fin_l=1
#                    elif ( detect_pic == -1 and debut_l==0 and fin_l==1):
#                        posLine1 = (i+index_debut_l)/2  
#                        break
#                    elif ((i-index_debut_l) >=20):
#                        debut_l=0
#                        fin_l=0



#ser.close()
#from CarGUI import *


#interface = GUI()
#try: initUART()
#except: 
#		print("Port serie non connecte")
#		interface.termtxt.insert(END, "Port serie non connecte!")
		
#fenetre.mainloop()
#fenetre.destroy()