# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 20:18:48 2014

@author: jerome
"""

# rajouter option save/load parameters...

from mtTkinter import * #Protection form thread crash
#from Tkinter import *
from tkFileDialog import asksaveasfilename
from tkFileDialog import askopenfilename
from ttk import *

from logger import *

import pickle as pickle 
import os
class GUI(Tk):
     
     def __init__(self, master):
          # variables: 
          self.stop_en=False
          self.hold_en = False
          #self.sendtxt=StringVar()
          # création fenetre:
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
          
      

          
         
          
          #topFrame  
          # Combobox(liste déroulante)
          self.labelcombobox = Label(self.topFrame, text="Mode : ").grid(sticky=N+W+S, in_=self.topFrame, row=0, column=0)
          self.listemodes = StringVar()
          self.MODES = ('DEBUG', 'RUN')
          self.combobox=Combobox(self.topFrame, textvariable = self.listemodes, values = self.MODES, state = 'readonly', \
                                 width = 10)
          self.listemodes.set(self.MODES[0]) #selection du premier choix à l'ouverture par defaut
          self.combobox.grid(sticky = N+W+S, in_ =self.topFrame , row=0, column=1)
          self.combobox.bind('<<ComboboxSelected>>', self.hello)    # Executer une méthode -après- sélection d'un élément
          
          # bouton controle text UART:
          
          #self.style= Style().configure("2state.TButton", relief=SUNKEN) 
          
          self.button_log = Button(self.topFrame, text="Log" , command= self.displayLog)
          self.button_log.grid( in_ = self.topFrame, row=0, column = 2, sticky= 'W')      
          
          self.button_line = Button(self.topFrame, text="Line")
          self.button_line.grid( in_ = self.topFrame, row=0, column = 3, sticky= 'W')      
          
          self.button_pause = Button(self.topFrame, text="Stop", command=self.StopUART )
          self.button_pause.grid( in_ = self.topFrame, row=0, column = 6, sticky = 'WN')
          
          self.button_hold = Button(self.topFrame, text="Hold" , command= self.Holdtxt)
          self.button_hold.grid( in_ = self.topFrame, row=0, column = 7, sticky= 'WN')
         
		
  
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
          self.ofst_vitLabel = Label(self.ofst_vitFrame, text="Vitesse min:")
          self.ofst_vitLabel.grid( sticky=W+N+S, in_=self.ofst_vitFrame, column=0)
          self.offset_vit = Spinbox(self.ofst_vitFrame, from_=0.0, to=1.0,increment=0.01, width=5)
          self.offset_vit.grid(sticky=N+E+S, in_=self.ofst_vitFrame, column=1, row=0)
                   
         
          self.max_vitLabel = Label(self.ofst_vitFrame, text="Vitesse max:")
          self.max_vitLabel.grid( sticky=W+N+S, in_=self.ofst_vitFrame, column=0)
          self.vit_max = Spinbox(self.ofst_vitFrame, from_=0.0, to=1.0,increment=0.01, width=5)
          self.vit_max.grid(sticky=N+E+S, in_=self.ofst_vitFrame, column=1, row=1)



          #pid diff 
          self.PIDdiff = LabelFrame(self.paramFrame,width=160,height=50,borderwidth=5, text="PID DIFF")
          self.PIDdiff.grid( sticky=W+N+S+E,row=4, in_=self.paramFrame)
          
          self.PdLabel = Label(self.PIDdiff, text="P: ")
          self.PdLabel.grid( sticky='E', in_=self.PIDdiff, row=0, column=0)
          self.Pdspbx = Spinbox(self.PIDdiff, from_=0.0000, to=1.0000,increment=0.0002, width=7)
          self.Pdspbx.grid(sticky='W', in_=self.PIDdiff, column=1, row=0)
          
          self.IdLabel = Label(self.PIDdiff, text="I: ")
          self.IdLabel.grid( sticky='E', in_=self.PIDdiff, row=1, column=0)
          self.Idspbx = Spinbox(self.PIDdiff, from_=0.0, to=1.0,increment=0.01, width=5)
          self.Idspbx.grid(sticky=W, in_=self.PIDdiff, column=1, row=1)
          
          self.DdLabel = Label(self.PIDdiff, text="D: ")
          self.DdLabel.grid( sticky='E', in_=self.PIDdiff, row=2, column=0)
          self.Ddspbx = Spinbox(self.PIDdiff, from_=0.0, to=1.0,increment=0.01, width=5)
          self.Ddspbx.grid(sticky=W, in_=self.PIDdiff, column=1, row=2)  
          
          
          #Seuil de la camera
          self.seuilLabel = Label(self.paramFrame, text="Seuil dérivé :")
          self.seuilLabel.grid( sticky='W', row=5, column=0)
          self.seuil = Spinbox(self.paramFrame, from_=0, to=1000,increment=20, width=5)
          self.seuil.grid(sticky=E,  column=0, row=5)  
          
          
          
          #Bouton Send config
          self.bouton_sendConf = Button(self.paramFrame, text="Envoyer", command=self.autoSave)
          self.bouton_sendConf.grid(in_=self.paramFrame, row=6,sticky = 'SWE')
          
          
          # Bouton refresh:		      
          self.bouton_maj = Button(self.paramFrame, text="Refresh", command=self.writePS)
          self.bouton_maj.grid(in_=self.paramFrame, row=7,sticky = 'SWE')
          
          
          #varFrame:
          self.vartitle = Label(self.varFrame, text="Variables: ").grid( sticky=W+N+S, in_=self.varFrame)
          
          
          
          #termFrame :
          # Zone de texte:      
          self.scrollbar = Scrollbar(self.termFrame)
          self.scrollbar.grid(sticky = 'WNS', row=1, column = 1)			   
          self.termtxt = Text(self.termFrame, width=40, yscrollcommand=self.scrollbar.set)
          self.termtxt.grid(row=1, in_=self.termFrame, sticky = 'EWSN')
          self.termtxt.tag_config('send',foreground='#00008c')
          self.termtxt.tag_config('receive',foreground='#008c00')
          self.scrollbar.config( command=self.termtxt.yview)
          
          
          # bouton reset Port série:
          self.bouton_rstPS = Button(self.termFrame, text="Reset", command=None)#self.resetPS)
          self.bouton_rstPS.grid(in_=self.termFrame, row=3,sticky = 'SE')
          
          # bouton envoyer:
          self.bouton_sendPS = Button(self.termFrame, text="Envoyer", command=None)#self.sendPS)
          self.bouton_sendPS.grid(in_=self.termFrame, row=3,sticky = 'SW') 
          
          # zone d'envoie:
          self.entryPS = Entry(self.termFrame )
          self.entryPS.grid(in_=self.termFrame, row=2, sticky = 'EW')
          
          
          # Layout main Frames : 
          self.topFrame.grid(row=0, columnspan=7,sticky='EWN')
          self.paramFrame.grid(row=1, column=0, sticky='EWSN')
          self.varFrame.grid(row=1, column=1, sticky='EWSN')
          self.termFrame.grid(row=1, column = 2, sticky='EWSN') 
          
          # Allowing cell/widget resizing:
          self.grid_columnconfigure(2,weight=2)
          self.grid_rowconfigure(1,weight=1)
          #self.topFrame.grid_columnconfigure(2,weight=2)
          self.topFrame.grid_columnconfigure(4,weight=2)
          #self.topFrame.grid_columnconfigure(2,weight=2)
          self.termFrame.grid_columnconfigure(0,weight=2)
          self.termFrame.grid_rowconfigure(1,weight=1)   
          self.paramFrame.grid_rowconfigure(7,weight=2)
          
          self.grid_columnconfigure(1, weight=1)
         
         
         
          #menu bar:
          self.menubar = Menu(self)
          self.menu1= Menu(self.menubar, tearoff=0)
          self.menu1.add_command(label="Open Camera view", command=None)
          self.menu1.add_command(label="quitter", command=self.quit)
          self.menubar.add_cascade(label="Menu", menu=self.menu1)
          
          self.config(menu=self.menubar) #display the menu
          #Menu bar 
          self.filemenu = Menu(self, tearoff=0)
          self.filemenu.add_command(label="Save", command=self.save)
          self.filemenu.add_command(label="Open", command=self.load)
          self.menubar.add_cascade(label="File", menu=self.filemenu)




          #If autosave file exist load it 
          if (os.path.isfile("auto_save")) : 
               self.load("auto_save")


     def writePS(self,string="test ", tag = ""):    
          if self.stop_en == False: 
              
               self.termtxt.insert(END, string, tag)
               if self.hold_en == False:
                    self.termtxt.see(END)
                             


     
     def resetPS(self, *j):
          self.termtxt.delete(1.0, END)
          print('reset PS')
          
     def sendPS(self, *j):
          #print('send :'+self.entryPS.get())
          
         self.writePS('>>'+self.entryPS.get()+'\n\r', "send")
         return self.entryPS.get()+'\n\r'
         
     def StopUART(self, *j):
          self.stop_en = not self.stop_en
          if self.stop_en:
               self.button_pause.config( text='Start')#relief=RAISED )
          else:
               self.button_pause.config( text='Stop')#relief='SUNKEN')
               

     def Holdtxt(self, *j):
          self.hold_en = not self.hold_en
          if self.hold_en:
               self.button_hold.configure( underline=0)
               self.button_hold.state(statespec = ('active', 'pressed'))
          else :
               self.button_hold.config( underline=-1)
               
     def displayLog (self): 
          MyLog = log()
          data, legend = MyLog.readLogFile("logPython.txt")

          
          MyLog.display(data, legend)
     def hello(*j):
          print('hello')

     def save(self, fileName ="", *j): 

          if (fileName == ""):
               fileName =  asksaveasfilename()

          
          data = {};
          data['DIR_P'] = str(self.Ppspbx.get())
          data['DIR_I'] = str(self.Ipspbx.get())
          data['DIR_D'] = str(self.Dpspbx.get())
          
          data['SPE_P'] = str(self.Pvspbx.get())
          data['SPE_I'] = str(self.Ivspbx.get())
          data['SPE_D'] = str(self.Dvspbx.get())
          data['SPE_MIN'] = str( self.offset_vit.get())
          data['SPE_MAX'] = str(self.vit_max.get())
          
          data['DIFF_P'] = str(self.Pdspbx.get())
          data['DIFF_I'] = str(self.Idspbx.get())
          data['DIFF_D'] = str(self.Ddspbx.get())
          
          data['SEUIL'] = str(self.seuil.get())
          print "saving..."
          pickle.dump( data, open( fileName, "wb" ) )
                  
		  
		  
     def autoSave(self):
          print "auto saving..."
          self.save("auto_save")

		
     def load (self, fileName = "", *j):
          print "loading"
          if (fileName == ""):
               fileName =  askopenfilename()

          data = pickle.load(open(str(fileName), "rb" ))



          self.Ppspbx.delete(0,"end")
          self.Ppspbx.insert(0, data['DIR_P'])
          self.Ipspbx.delete(0,"end")
          self.Ipspbx.insert(0,  data['DIR_I'])
          self.Dpspbx.delete(0,"end")
          self.Dpspbx.insert(0, data['DIR_D'])
          
          
          self.Pvspbx.delete(0,"end")
          self.Pvspbx.insert(0,data['SPE_P'])
          self.Ivspbx.delete(0,"end")
          self.Ivspbx.insert(0,data['SPE_I'])
          self.Dvspbx.delete(0,"end")
          self.Dvspbx.insert(0,data['SPE_D'])
          self.offset_vit.delete(0,"end")
          self.offset_vit.insert(0,data['SPE_MIN'])
          self.vit_max.delete(0,"end")
          self.vit_max.insert(0,data['SPE_MAX'])
          
          self.Pdspbx.delete(0,"end")
          self.Pdspbx.insert(0,data['DIFF_P'])
          self.Idspbx.delete(0,"end")
          self.Idspbx.insert(0,data['DIFF_I'])
          self.Ddspbx.delete(0,"end")
          self.Ddspbx.insert(0,data['DIFF_D'])
          
          self.seuil.delete(0,"end")
          self.seuil.insert(0,data['SEUIL'])

		  
if __name__=="__main__":
     fenetre = GUI(None)
     fenetre.title('GUI Freescale Cup')
     # event : 
     fenetre.bouton_sendPS.bind("<Button-1>", fenetre.sendPS)
     fenetre.bouton_rstPS.bind("<Button-1>", fenetre.resetPS)
     fenetre.mainloop()
     fenetre.destroy()

		
		
    
