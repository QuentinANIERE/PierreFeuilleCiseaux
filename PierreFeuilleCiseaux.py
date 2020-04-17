from random import randint


#Arrivé dans le jeu
print('Bienvenue dans le jeu du "Pierre, Feuille, Ciseaux" !')
print() #Saut de ligne

#Fonction qui détermine le choix de l'ordi
def choixOrdi():
    choixPossibles = ["Pierre", "Feuille", "Ciseaux"]
    indexChoix = randint(0, 3)
    choixOrdi = choixPossibles[indexChoix]

