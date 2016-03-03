# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 20:18:48 2014

@author: jerome
"""


from Tkinter import *
from ttk import *

class GUI(Tk):
	
     def __init__(self, master):
         Tk.__init__(self,master)
         self.master = master
         self.initialize()
         
     def initialize(self):
         self.minsize(width=500, height=300)
         self.grid()
         
    # include WIDGETS # 
         #main frames:
         self.topFrame   = Frame(self, borderwidth=2, relief=RAISED)
         self.paramFrame = Frame(self, borderwidth=2, relief=RAISED)
         self.varFrame   = Frame(self, borderwidth=2, relief=RAISED)
         self.termFrame  = Frame(self, borderwidth=2, relief=RAISED)
  
      
         #menu bar:
         self.menubar = Menu(self)
         self.menu1= Menu(self.menubar, tearoff=0)
         self.menu1.add_command(label="quitter", command=self.quit)
         self.menu1.add_command(label="(vide)")
         self.menubar.add_cascade(label="Menu", menu=self.menu1)
		
         self.config(menu=self.menubar) #display the menu
  
        #topFrame  
             # Combobox(liste déroulante)
         self.labelcombobox = Label(self.topFrame, text="Mode : ").grid(sticky=N+W+S, in_=self.topFrame, row=1, column=0)
         self.listemodes = StringVar()
         self.MODES = ('DEBUG', 'RUN')
         self.combobox=Combobox(self.topFrame, textvariable = self.listemodes, values = self.MODES, state = 'readonly', \
							width = 10)
         self.listemodes.set(self.MODES[0]) #selection du premier choix à l'ouverture par defaut
         self.combobox.grid(sticky = N+W+S, in_ =self.topFrame , row=1, column=1)
         self.combobox.bind('<<ComboboxSelected>>', self.hello)    # Executer une méthode -après- sélection d'un élément
		
  
         #paramFrame: 
              #pid pos
         self.PIDpos = LabelFrame(self.paramFrame,width=160,height=50,borderwidth=5, text="PID POS")
         self.PIDpos.grid( sticky=W+N+S+E,row=0, in_=self.paramFrame)
		
         self.PpLabel = Label(self.PIDpos, text="P: ")
         self.PpLabel.grid( sticky=E, in_=self.PIDpos, row=0, column=0)
         self.Ppspbx = Spinbox(self.PIDpos, from_=0.0, to=1.0,increment=0.01, width=5)
         self.Ppspbx.grid( in_=self.PIDpos, column=1, row=0)
		
         self.IpLabel = Label(self.PIDpos, text="I: ")
         self.IpLabel.grid( sticky=E, in_=self.PIDpos, row=1, column=0)
         self.Ipspbx = Spinbox(self.PIDpos, from_=0.0, to=1.0,increment=0.01, width=5)
         self.Ipspbx.grid( in_=self.PIDpos, column=1, row=1)
		
         self.DpLabel = Label(self.PIDpos, text="D: ")
         self.DpLabel.grid( sticky=E, in_=self.PIDpos, row=2, column=0)
         self.Dpspbx = Spinbox(self.PIDpos, from_=0.0, to=1.0,increment=0.01, width=5)
         self.Dpspbx.grid( in_=self.PIDpos, column=1, row=2)
  
  
              #pid vit
         self.PIDvit = LabelFrame(self.paramFrame,width=160,height=50,borderwidth=5, text="PID VIT")
         self.PIDvit.grid( sticky=W+N+S+E,row=1, in_=self.paramFrame)
		
         self.PvLabel = Label(self.PIDvit, text="P: ")
         self.PvLabel.grid( sticky='E', in_=self.PIDvit, row=0, column=0)
         self.Pvspbx = Spinbox(self.PIDvit, from_=0.0, to=1.0,increment=0.01, width=5)
         self.Pvspbx.grid(sticky='W', in_=self.PIDvit, column=1, row=0)
		
         self.IvLabel = Label(self.PIDvit, text="I: ")
         self.IvLabel.grid( sticky='E', in_=self.PIDvit, row=1, column=0)
         self.Ivspbx = Spinbox(self.PIDvit, from_=0.0, to=1.0,increment=0.01, width=5)
         self.Ivspbx.grid(sticky=W, in_=self.PIDvit, column=1, row=1)
		
         self.DvLabel = Label(self.PIDvit, text="D: ")
         self.DvLabel.grid( sticky='E', in_=self.PIDvit, row=2, column=0)
         self.Dvspbx = Spinbox(self.PIDvit, from_=0.0, to=1.0,increment=0.01, width=5)
         self.Dvspbx.grid(sticky=W, in_=self.PIDvit, column=1, row=2)  
  
  
              #enable pid vit
         self.enablePIDv = IntVar()
         self.CHKBOXpidvit = Checkbutton(self.paramFrame, text="PID VIT enable", variable=self.enablePIDv)
         self.CHKBOXpidvit.grid(sticky=N+W+S,row=2, in_=self.paramFrame)
		
        	   #offset vitesse
         self.ofst_vitFrame = Frame(self.paramFrame,borderwidth=2, relief=RAISED)
         self.ofst_vitFrame.grid(sticky=N+W+S,row=3, in_=self.paramFrame)
         self.ofst_vitLabel = Label(self.ofst_vitFrame, text="Offset Vitesse:")
         self.ofst_vitLabel.grid( sticky=W+N+S, in_=self.ofst_vitFrame, column=0)
         self.offset_vit = Spinbox(self.ofst_vitFrame, from_=0.0, to=1.0,increment=0.01, width=5)
         self.offset_vit.grid(sticky=N+E+S, in_=self.ofst_vitFrame, column=1, row=0)


               # Bouton refresh:		      
         self.bouton_maj = Button(self.paramFrame, text="Refresh", command="")#resetUART)
         self.bouton_maj.grid(in_=self.paramFrame, row=4,sticky = 'SWE')
        
		
         #varFrame:
         self.vartitle = Label(self.varFrame, text="Variables: ").grid( sticky=W+N+S, in_=self.varFrame)
		
  
         #termFrame :
               # Zone de texte:         
         self.termtxt = Text(self.termFrame, width=40)
         self.termtxt.grid(row=1, in_=self.termFrame, sticky = 'EWSN')
         
         
         # Layout main Frames : 
         self.topFrame.grid(row=0, sticky='EWN')
         self.paramFrame.grid(row=1, column=0, sticky='EWSN')
         self.varFrame.grid(row=1, column=1, sticky='EWSN')
         self.termFrame.grid(row=1, column = 2, sticky='EWSN') 
		
             # Allowing cell/widget resizing:
         self.grid_columnconfigure(2,weight=2)
         self.grid_rowconfigure(1,weight=1)
         self.termFrame.grid_columnconfigure(0,weight=2)
         self.termFrame.grid_rowconfigure(1,weight=1)   
         self.paramFrame.grid_rowconfigure(4,weight=2)
  
         self.grid_columnconfigure(1, weight=1)
         
         
     def hello(*j):
          print('hello')
          
          
if __name__=="__main__":
    fenetre = GUI(None)
    fenetre.title('GUI Freescale Cup')
    fenetre.mainloop()
    fenetre.destroy()

		
		
    