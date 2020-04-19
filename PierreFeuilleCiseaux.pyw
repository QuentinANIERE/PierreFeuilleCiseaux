import os
from tkinter import *
from random import randint
import tkinter.font as tkFont

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


#On crée un cadre pour contenir les images
cadre = Frame(fen, bg="Grey")
cadre.pack(side=BOTTOM, pady=10)     

#Fonction qui sera executé si on clique sur la pierre
def clicPierre(p):
    jeu("pierre")

#On met l'image dans label afin de pouvoir utiliser la méthode bind
pierre = Label(fen, bg="grey", image=photoPierre)
pierre.pack(side=LEFT, padx=50)
pierre.bind('<Button-1>', clicPierre) 

#Fonction qui sera executé si on clique sur la feuille
def clicFeuille(f):
    jeu("feuille")

#On met l'image dans label afin de pouvoir utiliser la méthode bind
feuille = Label(fen, bg="grey", image=photoFeuille)
feuille.pack(side=LEFT, padx=10)
feuille.bind('<Button-1>', clicFeuille) 

#Fonction qui sera executé si on clique sur la feuille
def clicCiseaux(c):
    jeu("ciseaux")

#On met l'image dans label afin de pouvoir utiliser la méthode bind
ciseaux = Label(fen, bg="grey", image=photoCiseaux)
ciseaux.pack(side=LEFT, padx=50)
ciseaux.bind('<Button-1>', clicCiseaux) 

#Fonction qui détermine le choix de l'ordi
def choixOrdi():
    choixPossibles = ["pierre", "feuille", "ciseaux"]
    indexChoix = randint(0, 2)
    choixDeOrdi = choixPossibles[indexChoix]
    return choixDeOrdi

#Fonction rejouer
def rejouer():
    global policeTitre, titre, sousTitre, labelScore, bouttonRejouer, cadre, pierre, feuille, ciseaux

    #On fait disparaitre tout l'affichage de la partie précédente
    titre.pack_forget()
    sousTitre.pack_forget()
    labelScore.pack_forget()
    bouttonRejouer.pack_forget()

    #On fait re-appaitre le cadre et les bouttons
    cadre.pack(side=BOTTOM, pady=10)
    pierre.pack(side=LEFT, padx=50)
    feuille.pack(side=LEFT, padx=10)
    ciseaux.pack(side=LEFT, padx=50)

#Polices personalisées pour le titre et le sous titre
policeTitre = tkFont.Font(family="Verdanna",size=24,weight="bold")
policeSousTitre = tkFont.Font(family="Times", size=16)

#Fonction qui affiche le résultat
def afficher(choixDeOrdi, victoire):
    global policeTitre, titre, sousTitre, labelScore, bouttonRejouer, score

    #Le titre
    titre = Label(fen, bg="Grey", font=policeTitre, text=" ")

    if victoire == True:
        titre.configure(text="Bravo !")
        score += 1
    elif victoire == False:
        titre.configure(text="Perdu...")
    else:
       titre.configure(text="Égalité !")

    titre.pack(side=TOP, pady=10)    

    #On sauvegarde le score dans un fichier txt
    fichier = open("sauvegarde.txt", "w")
    fichier.write(str(score)) #On oublie pas de convertir le score en string
    fichier.close()

    #Le "sous titre"
    texteSousTitre = "L'ordinateur avait choisi " + choixDeOrdi + "."
    sousTitre = Label(fen, bg="Grey", text=texteSousTitre, font=policeSousTitre)
    sousTitre.pack()

    #Le score
    texteScore = "Votre score est de " + str(score) +"."
    labelScore = Label(fen, bg="Grey", text=texteScore)
    labelScore.pack()

    #Le bouton rejouer
    bouttonRejouer = Button(fen, text="Rejouer", command=rejouer)
    bouttonRejouer.pack(side=BOTTOM, pady=15)

#Fonction qui contient le jeu en lui même
def jeu(choixDeUser):
    global score, pierre, feuille, ciseaux

    choixDeOrdi = choixOrdi()
    
    #On efface le cadre et les bouttons afin de pouvoir afficher le résultat prochainement 
    pierre.pack_forget()
    feuille.pack_forget()
    ciseaux.pack_forget()
    cadre.pack_forget()

    #En cas d'égalité
    if  choixDeUser == choixDeOrdi:
        afficher(choixDeOrdi, "Null")

    #Bloc if si le choix de l'ordi est "Pierre"
    if choixDeOrdi == "pierre" and choixDeUser == "feuille" and choixDeUser != choixDeOrdi:
        afficher(choixDeOrdi, True)
    elif choixDeOrdi == "pierre" and choixDeUser != "feuille" and choixDeUser != choixDeOrdi:
        afficher(choixDeOrdi, False)

    #Bloc if si le choix de l'ordi est "Feuille"
    if choixDeOrdi == "feuille" and choixDeUser == "ciseaux" and choixDeUser != choixDeOrdi:
       afficher(choixDeOrdi, True)
    elif choixDeOrdi == "feuille" and choixDeUser != "ciseaux" and choixDeUser != choixDeOrdi:
        afficher(choixDeOrdi, False)

    #Bloc if si le choix de l'ordi est "Ciseaux"
    if choixDeOrdi == "ciseaux" and choixDeUser == "pierre" and choixDeUser != choixDeOrdi:
       afficher(choixDeOrdi, True)
    elif choixDeOrdi == "ciseaux" and choixDeUser != "pierre" and choixDeUser != choixDeOrdi:
        afficher(choixDeOrdi, False)

fen.mainloop()