import os
import time
import platform
from tkinter import *
from random import randint

#On défini la fênetre du jeu
fen = Tk()
fen.geometry("450x175")
fen.resizable(width=False, height=False)
fen.title("Pierre, Feuille, Ciseaux !")
fen.configure(bg="grey")
fen.iconbitmap(bitmap="medias/icone.ico")

#On récupére le score dans le ficher sauvegarde.txt
if os.path.isfile("sauvegarde.txt"):
    fichier = open("sauvegarde.txt", "r")
    score = int(fichier.read())
else:
    score = 0

#Lecture de photos
photoPierre = PhotoImage(file="medias/pierre.png")
photoFeuille = PhotoImage(file="medias/feuille.png")
photoCiseaux = PhotoImage(file="medias/ciseaux.png")

cadre = Frame(fen, bg="Grey")
cadre.pack(side=BOTTOM, pady=10)     

def clicpierre(p):
    print("Pierre !")

pierre = Label(fen, bg="grey", image=photoPierre)
pierre.pack(side="left", padx=50)
pierre.bind('<Button-1>', clicpierre) 

def clicfeuille(p):
    print("Feuille !")

feuille = Label(fen, bg="grey", image=photoFeuille)
feuille.pack(side=LEFT, padx=10)
feuille.bind('<Button-1>', clicfeuille) 


















#Fonction qui détermine le choix de l'ordi
def choixOrdi():
    choixPossibles = ["Pierre", "Feuille", "Ciseaux"]
    indexChoix = randint(0, 2)
    choixDeOrdi = choixPossibles[indexChoix]
    return choixDeOrdi

#On vérifie que l'entrée de l'user est correcte 
listeEntresCorrectes = ["Pierre", "pierre", "p", "Feuille", "feuille", "f", "Ciseaux", "ciseaux", "ciseau","Ciseau", "c"]
listeEntresValide = ["Pierre", "Feuille", "Ciseaux"] #Cette liste contient les entrées pouvant être comparées à celle de l'ordi

#On écrit le score dans un fichier txt
fichier = open("sauvegarde.txt", "w")
fichier.write(str(score)) #On oublie de convertir le score en string
fichier.close()

#Fonction qui contient le jeu en lui même
def jeu():
    global score

    #En cas d'égalité
    if  choixDeUser == choixDeOrdi:
        print("Égalité !")
        rejouer()

    #Bloc if si le choix de l'ordi est "Pierre"
    if choixDeOrdi == "Pierre" and choixDeUser == "Feuille" and choixDeUser != choixDeOrdi:
        print("L'ordinateur à choisi", choixDeOrdi + ". Vous avez gagné !")
        score += 1
        rejouer()
    elif choixDeOrdi == "Pierre" and choixDeUser != "Feuille" and choixDeUser != choixDeOrdi:
        print("L'ordinateur à choisi", choixDeOrdi +". L'ordinateur a gagné...")
        rejouer()

    #Bloc if si le choix de l'ordi est "Feuille"
    if choixDeOrdi == "Feuille" and choixDeUser == "Ciseaux" and choixDeUser != choixDeOrdi:
       print("L'ordinateur à choisi", choixDeOrdi + ". Vous avez gagné !")
       score += 1
       rejouer()
    elif choixDeOrdi == "Feuille" and choixDeUser != "Ciseaux" and choixDeUser != choixDeOrdi:
        print("L'ordinateur à choisi", choixDeOrdi +". L'ordinateur a gagné...")
        score += 1
        rejouer()

    #Bloc if si le choix de l'ordi est "Ciseaux"
    if choixDeOrdi == "Ciseaux" and choixDeUser == "Pierre" and choixDeUser != choixDeOrdi:
        print("L'ordinateur à choisi", choixDeOrdi + ". Vous avez gagné !")
        score += 1
        rejouer()
    elif choixDeOrdi == "Ciseaux" and choixDeUser != "Pierre" and choixDeUser != choixDeOrdi:
        print("L'ordinateur à choisi", choixDeOrdi +". L'ordinateur a gagné...")
        rejouer()

fen.mainloop()