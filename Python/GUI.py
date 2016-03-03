# -*- coding: utf-8 -*-
from Tkinter import *
from ttk import *

class Interface:
    
    """Notre fenetre principale.
    Tous les widgets sont stockés comme attributs de cette fenetre."""    
    
    def __init__(self, master):
        """
        cv = Canvas(master, width=500, height=600)
        cv.pack()
        
        cv.create_line(0, 0, 200, 100)
        cv.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
        cv.create_rectangle(50, 25, 150, 75, fill="blue")
        """
        master.minsize(width=500, height=300)
        #frame = Frame(master, width=500, height=300,relief=SUNKEN, colormap="new")
        #frame.pack()
        
        # Création de nos widgets
        self.message = Label(master, text="Vous n'avez pas cliqué sur le bouton.")
        self.message.grid(row=0)
        
        self.bouton_quitter = Button(master, text="Quitter", command=master.quit)
        self.bouton_quitter.grid(row=1, column=0)
        
        self.bouton_cliquer = Button(master, text="Cliquez ici", fg="red",
                command=self.cliquer)
        self.bouton_cliquer.grid(row=3, column=1)
    
    def cliquer(self):
        """Il y a eu un clic sur le bouton.
        
        On change la valeur du label message."""
        self.message["text"] = "Vous avez cliqué {} fois.".format(2)
        
        
fenetre = Tk()
interface = Interface(fenetre)
fenetre.mainloop()
fenetre.destroy()