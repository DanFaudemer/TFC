# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 20:18:48 2014

@author: jerome
"""

import os
import tkinter as Tk
import tkinter.ttk as ttk
import subprocess as sp
import serial
from time import sleep
#import sys
import threading 
from pubsub import pub
from serial.tools.list_ports import comports

class Term(serial.Serial, Tk.Frame):
    def __init__(self,parent, **kwargs):
        serial.Serial.__init__(self,**kwargs)
        Tk.Frame.__init__(self,parent,**kwargs)
        self.parent=parent
        self.threadSer = threading.Thread(target=self.r_thread)
        self.first_sread=0
        self.sendlist = []
        self.ind = 0
        self.ind_mem=0
        for i in range(30):
            self.sendlist.append("")
        
        self.getportlist = serial.tools.list_ports.comports()
        self.ports=[]
        self.ports_desc=[]
        for p, desc, hwid in self.getportlist:
            self.ports.append(p)
            self.ports_desc.append(desc)
        
        
        pub.subscribe(self.print_term,'write_term')
        
    def open_port(self):#, port, baudrate):
        for port in self.ports:
            if(self.PortCOM.get().find(port) >= 0 ):
                self.port=port
        self.baudrate=self.Baudrate.get() #baudrate
        self.timeout=2
        try:
            self.open()
            print('Open : ok')
            self.termtxt.insert(Tk.END,'['+ self.port+" open]"+'\n') 
            self.sread()
        except:
            print('Open : Err')
            self.termtxt.insert(Tk.END,'['+ self.port+" err]"+'\n') 
        self.termtxt.see(Tk.END)
        
        
    def send(self,*args): #,string,**kwargs):
        #print(self.ind)
        self.fail=0
        try:
            self.write(bytes(self.TextSend.get()+'\r'+'\n','UTF-8'))
        except:
            print(">> [err write]")
            self.termtxt.insert(Tk.END, "Err: Can't send data \n")
            self.fail=1
            
        if(self.fail==0 and self.TextSend.get()!=''):
            print('Tx: '+self.TextSend.get())
            
            self.termtxt.insert(Tk.END, "Tx: "+self.TextSend.get()+'\n') 
            self.sendlist[self.ind]=self.TextSend.get()
            self.ind=(self.ind+1)%30
            self.ind_mem=self.ind
            self.TextSend.set('')
        self.termtxt.see(Tk.END)
    
        
    def sread(self):
        if(self.first_sread==0):
            self.threadSer.start()
            self.first_sread=1
    
    
    def print_term(self, string):
        print('Rx: ',string.decode("UTF-8"))
        self.termtxt.insert(Tk.END, 'Rx: '+string.decode("UTF-8")) 
        self.termtxt.see(Tk.END)
        #print(string)
        
    def r_thread(self):
        while(1):
            try:
                string=self.readline()
            except:
                string=b''
            if(string != b''):
                pub.sendMessage('write_term', string=string)
                #print("Term: ",string.decode("utf-8"))
            sleep(0.1)
        #self.threadSer.stop()
        
    def CloseSer(self):
        if self.isOpen():
            self.close()
            print('['+self.port+' closed]')
            self.termtxt.insert(Tk.END, '['+self.port+' closed]\n') 
            self.termtxt.see(Tk.END)

    def nav_mem(self,dir, *args):
        #print(dir)
        if(dir=="up"):
            if(self.sendlist[(self.ind_mem-1)%30]!=''):
                self.ind_mem=(self.ind_mem-1)%30
        elif(dir=="down"):
            if(self.sendlist[(self.ind_mem+1)%30]!=''):
                self.ind_mem=(self.ind_mem+1)%30
        self.TextSend.set(self.sendlist[self.ind_mem])
        print(self.ind_mem)
   
    def gui(self):
        self.parent.title("Terminal")
        
        self.Frame_top = Tk.Frame(self.parent)
        self.Frame_body = Tk.Frame(self.parent)
        # labels:
        self.label_PortCom = Tk.Label(self.Frame_top, text="  PortCOM: ")
        self.label_Baudrate = Tk.Label(self.Frame_top, text="     Baudrate: ")
        
        # champ de saisi:
        self.PortCOM= Tk.StringVar()
        #self.Entry_PortCom = Tk.Entry(self.Frame_top, textvariable=self.PortCOM, width=10)
        self.CB_Ports = ttk.Combobox(self.Frame_top, textvariable=self.PortCOM, values=self.ports_desc)
        self.PortCOM.set(self.ports_desc[0])
         
        self.Baudrate= Tk.StringVar()
        self.Entry_BaudRate = Tk.Entry(self.Frame_top, textvariable=self.Baudrate, width=10)
        self.Baudrate.set('9600')
        
        self.TextSend= Tk.StringVar()
        self.Entry_Send = Tk.Entry(self.Frame_body, textvariable=self.TextSend)
        
        # Zone de texte:      
        self.scrollbar = Tk.Scrollbar(self.Frame_body)
        self.termtxt = Tk.Text(self.Frame_body, width=60, heigh=20, yscrollcommand=self.scrollbar.set)
        #termtxt.tag_config('send',foreground='#00008c')
        #termtxt.tag_config('receive',foreground='#008c00')
        self.scrollbar.config( command=self.termtxt.yview)
        
        #button
        self.bouton_Open = Tk.Button(self.Frame_body, text="Open", command=self.open_port)
        self.bouton_Close = Tk.Button(self.Frame_body, text="Close", command=self.CloseSer)
        self.bouton_Send = Tk.Button(self.Frame_body, text="Send", command=self.send)
    
        #pack:
        self.Frame_top.grid(row=0, sticky='NEW', padx=3,pady=3)
        self.Frame_body.grid(row=1, sticky='NEWS')
        self.label_PortCom.grid(in_=self.Frame_top, column=0, row=0, sticky='NSE')
        self.label_Baudrate.grid(in_=self.Frame_top, column=2, row=0, sticky='NSE')
        self.CB_Ports.grid(in_=self.Frame_top, column=1, row=0, sticky='NESW')
        self.Entry_BaudRate.grid(in_=self.Frame_top, column=3, row=0, sticky='NWS')
        self.scrollbar.grid(in_=self.Frame_body, sticky = 'WNS', row=0, column = 1, rowspan=3)
        self.termtxt.grid(row=0,column=0, sticky = 'EWSN', rowspan=3)
        self.bouton_Open.grid(in_=self.Frame_body,row=0, column=2,sticky='NW')
        self.bouton_Close.grid(in_=self.Frame_body,row=1, column=2,sticky='NW')
        self.Entry_Send.grid(in_=self.Frame_body, row=3, column=0, columnspan=2, sticky='EWN', padx=3,pady=3)
        self.bouton_Send.grid(in_=self.Frame_body,row=3, column=2,sticky='WS')
        
       #resizing:
        self.parent.grid_columnconfigure(0, weight=1)
        self.parent.grid_rowconfigure(1, weight=1)
        self.Frame_body.grid_columnconfigure(0,weight=1)
        self.Frame_body.grid_rowconfigure(1,weight=1)
        self.Frame_top.grid_columnconfigure(1,weight=1)
        
        #event:
        self.parent.bind("<Return>", self.send)
        self.parent.bind("<Up>", lambda event, arg="up": self.nav_mem(arg))
        self.parent.bind("<Down>", lambda event, arg="down": self.nav_mem(arg))
        
if __name__=="__main__":
    root = Tk.Tk()
    term=Term(root)
    term.gui()
    print("Var : term")
    print(term)
    root.mainloop()
    root.destroy()

    #term.open_port('COM5',9600)
    
