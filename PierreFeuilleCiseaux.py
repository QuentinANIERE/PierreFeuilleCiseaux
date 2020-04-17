from random import randint

#Message de bienvenue
print('Bienvenue dans le jeu du "Pierre, Feuille, Ciseaux" !')
print() #Saut de ligne

#Fonction qui détermine le choix de l'ordi
def choixOrdi():
    choixPossibles = ["Pierre", "Feuille", "Ciseaux"]
    indexChoix = randint(0, 3)
    choixDeOrdi = choixPossibles[indexChoix]
    return choixDeOrdi

#Fonction qui demande à l'user son choix et vérifie si l'entrée est valide
def choixUser():
    global choixDeUser
    choixDeUser = input("Que voulez faire ? (Pierre, Feuille, Ciseaux ?)\n>>> ")
    #On vérifie que l'entrée de l'user est correcte 
    listeEntresCorrectes = ["Pierre", "pierre", "p", "Feuille", "feuille", "f", "Ciseaux", "ciseaux", "ciseau","Ciseau", "c"]
    if choixDeUser not in listeEntresCorrectes:
    #On vérifie si l'entrée de l'utilisateur n'est pas dans la liste des choix possibles
        print("Votre choix n'est pas valide !")
        print()
        choixUser()

choixUser()

#On affiche le résultat
print("Vous avez choisi", choixDeUser)
