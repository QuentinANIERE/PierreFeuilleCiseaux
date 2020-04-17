import os
import time
import platform
from random import randint

#On récupére le score dans le ficher sauvegarde.txt
if os.path.isfile("sauvegarde.txt"):
    fichier = open("sauvegarde.txt", "r")
    score = int(fichier.read())
else:
    score = 0

#Fonction qui permet d'effacer la console
def clear():
    if platform.system() == "Windows":
    #Si le script est executé sous windows
        os.system("cls")
    elif platform.system() == "Linux":
    #Si le script est executé sous Linux
        os.system("clear")

#Message de bienvenue
print('Bienvenue dans le jeu du "Pierre, Feuille, Ciseaux" !')
time.sleep(1.5)
clear()

#Fonction qui détermine le choix de l'ordi
def choixOrdi():
    choixPossibles = ["Pierre", "Feuille", "Ciseaux"]
    indexChoix = randint(0, 2)
    choixDeOrdi = choixPossibles[indexChoix]
    return choixDeOrdi

#Fonction qui demande à l'user son choix et vérifie si l'entrée est valide
def choixUser():
    choixDeUser = input("Que voulez faire ? (Pierre, Feuille, Ciseaux ?)\n>>> ")
    clear()

    #On vérifie que l'entrée de l'user est correcte 
    listeEntresCorrectes = ["Pierre", "pierre", "p", "Feuille", "feuille", "f", "Ciseaux", "ciseaux", "ciseau","Ciseau", "c"]
    listeEntresValide = ["Pierre", "Feuille", "Ciseaux"] #Cette liste contient les entrées pouvant être comparées à celle de l'ordi

    if choixDeUser not in listeEntresCorrectes:
    #On vérifie si l'entrée de l'utilisateur n'est pas dans la liste des choix possibles
        print("Votre choix n'est pas valide !")
        time.sleep(2)
        clear()
        choixUser()
    
    elif choixDeUser not in listeEntresValide:
    #Si l'entrée de l'utilisateur n'est pas au bon format
        if choixDeUser == "pierre" or choixDeUser == "p":
            choixDeUser = "Pierre"
        elif choixDeUser == "feuille" or choixDeUser == "f":
            choixDeUser = "Feuille"
        else: 
            choixDeUser = "Ciseaux"

    return choixDeUser

#Fonction qui demande à l'utilisateur si il veut rejouer 
def rejouer():
    #On efface l'affichage du résultat 
    time.sleep(2)
    clear()

    #On écrit le score dans un fichier txt
    fichier = open("sauvegarde.txt", "w")
    fichier.write(str(score)) #On oublie de convertir le score en string
    fichier.close()

    print("Votre score est actuellement de", str(score) +".")
    time.sleep(2)
    clear()

    choix = input("Voulez vous rejouer ? (Oui|Non) \n>>> ")
    clear()

    if choix == "Oui" or  choix == "oui" or  choix == "o" or choix == "O":
        jeu()

    elif choix == "Non" or choix == "non" or choix == "n" or choix == "N":
        print("Merci d'avoir joué, à bientôt !")
        time.sleep(2)
        clear()

    else:
        print("Votre choix n'est pas valide !")
        rejouer()

#Fonction qui contient le jeu en lui même
def jeu():
    global score
    #On inscrit le choix de l'user dans des variables afin qu'elle ne changent à chaque demande
    choixDeUser = choixUser()
    choixDeOrdi = choixOrdi()

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

jeu()


