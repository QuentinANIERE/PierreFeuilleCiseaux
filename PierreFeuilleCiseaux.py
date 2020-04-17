from random import randint

#Message de bienvenue
print('Bienvenue dans le jeu du "Pierre, Feuille, Ciseaux" !')
print() #Saut de ligne

#Fonction qui détermine le choix de l'ordi
def choixOrdi():
    choixPossibles = ["Pierre", "Feuille", "Ciseaux"]
    indexChoix = randint(0, 2)
    choixDeOrdi = choixPossibles[indexChoix]
    return choixDeOrdi

#Fonction qui demande à l'user son choix et vérifie si l'entrée est valide
def choixUser():
    choixDeUser = input("Que voulez faire ? (Pierre, Feuille, Ciseaux ?)\n>>> ")

    #On vérifie que l'entrée de l'user est correcte 
    listeEntresCorrectes = ["Pierre", "pierre", "p", "Feuille", "feuille", "f", "Ciseaux", "ciseaux", "ciseau","Ciseau", "c"]
    listeEntresValide = ["Pierre", "Feuille", "Ciseaux"] #Cette liste contient les entrées pouvant être comparées à celle de l'ordi

    if choixDeUser not in listeEntresCorrectes:
    #On vérifie si l'entrée de l'utilisateur n'est pas dans la liste des choix possibles
        print("Votre choix n'est pas valide !")
        print()
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
    print() #On laisse un ligne vide
    choix = input("Voulez vous rejouer ? (Oui|Non) \n>>> ")

    if choix == "Oui" or  choix == "oui" or  choix == "o":
        jeu()

    elif choix == "Non" or choix == "non" or choix == "n":
        print("Merci d'avoir joué, à bientôt !")
        input("Appuyer sur entrée pour quitter")

    else:
        print("Votre choix n'est pas valide !")
        rejouer()

#Fonction qui contient le jeu en lui même
def jeu():
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
        rejouer()
    elif choixDeOrdi == "Pierre" and choixDeUser != "Feuille" and choixDeUser != choixDeOrdi:
        print("L'ordinateur à choisi", choixDeOrdi +". L'ordinateur a gagné...")
        rejouer()

    #Bloc if si le choix de l'ordi est "Feuille"
    if choixDeOrdi == "Feuille" and choixDeUser == "Ciseaux" and choixDeUser != choixDeOrdi:
       print("L'ordinateur à choisi", choixDeOrdi + ". Vous avez gagné !")
       rejouer()
    elif choixDeOrdi == "Feuille" and choixDeUser != "Ciseaux" and choixDeUser != choixDeOrdi:
        print("L'ordinateur à choisi", choixDeOrdi +". L'ordinateur a gagné...")
        rejouer()

    #Bloc if si le choix de l'ordi est "Ciseaux"
    if choixDeOrdi == "Ciseaux" and choixDeUser == "Pierre" and choixDeUser != choixDeOrdi:
        print("L'ordinateur à choisi", choixDeOrdi + ". Vous avez gagné !")
        rejouer()
    elif choixDeOrdi == "Ciseaux" and choixDeUser != "Pierre" and choixDeUser != choixDeOrdi:
        print("L'ordinateur à choisi", choixDeOrdi +". L'ordinateur a gagné...")
        rejouer()

jeu()


