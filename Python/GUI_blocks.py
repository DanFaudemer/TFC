# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 20:18:48 2014

@author: jerome
"""


from Tkinter import *
from ttk import *

#from Tkinter.ttk import * # avec des themes 
# On crée une fenêtre, racine de notre interface
fen = Tk()

# Label : texte
champ_label = Label(fen, text="Salut les Zér0s !")
champ_label.pack()# On affiche le label dans la fenêtre

# bouton
bouton_Quit = Button(fen, text="quitter", command=fen.quit)
bouton_Quit.pack()

# champ de saisi
var_texte = StringVar()
ligne_texte = Entry(fen, textvariable=var_texte, width=30)
ligne_texte.pack() # methode trace peut etre executée a chaque fois que la variable est modifiée

# check box
var_case = IntVar()
case = Checkbutton(fen, text="Ne plus poser cette question", variable=var_case)
case.pack()
print(var_case.get())

#boutons radio
var_choix = StringVar()
choix_rouge = Radiobutton(fen, text="Rouge", variable=var_choix, value="rouge")
choix_vert = Radiobutton(fen, text="Vert", variable=var_choix, value="vert")
choix_bleu = Radiobutton(fen, text="Bleu", variable=var_choix, value="bleu")
choix_rouge.pack()
choix_vert.pack()
choix_bleu.pack()

#liste déroulante
framelist = Frame(fen)
scrollbar = Scrollbar(framelist, orient = VERTICAL)
liste = Listbox(framelist, selectmode=BROWSE, yscrollcommand = scrollbar.set, height=1)
scrollbar.config(command= liste.yview)
scrollbar.pack(side=RIGHT, fill=Y)
liste.pack(side=LEFT, fill=BOTH, expand = 4)
framelist.pack()
liste.insert(END, "Pierre")
liste.insert(END, "Feuille")
liste.insert(END, "Ciseau")
# >>> combobox: vraie liste déroulante (nécessite import de ttk 
listevar = StringVar()
values = ('choix1', 'choix2', 'choix3')
combobox=Combobox(fen, textvariable = listevar, values = values, state = 'readonly')
listevar.set(values[0])
combobox.pack()

print(liste.curselection()) #renvoie un tuple avec la position -1 de l'élément sélectionné

# frame 
cadre = Frame(fen, width=768, height=576, borderwidth=5)
cadre.pack(fill=BOTH)
message = Label(cadre, text="Notre fenêtre")
message.pack(side="right", fill=BOTH) #fill : X, Y or BOTH

#labelframe
cadre2 = LabelFrame(fen,width=120,height=50,borderwidth=5, text="Titre du cadre")
cadre2.pack(fill=BOTH)

#spinbox
w = Spinbox(fen, from_=0.0, to=1.0,increment=0.01)
w.pack()

# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
fen.mainloop()