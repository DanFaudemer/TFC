import serial
import sys
ser = serial.Serial("COM4", baudrate=115200)  # open first serial port
print ser.portstr       # check which port was really used
channel1=[0]*128
channel2=[0]*128
while 0 :
    response = ser.readline().replace("L:"," ")
    response = response.split(',')
    print(len(response))
    if ( len(response) == 256) :
        for i in range(0, 127):
            channel1[i] = int(response[i],0)
        for i in range(128, 255):
            channel2[i-128] = int(response[i],16)
        #print (channel2)
    #sys.stdout.write(response)
    print ("-------------------")

while 1 :
        sys.stdout.write(ser.read())
