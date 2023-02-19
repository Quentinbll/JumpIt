from random import *

def genererSuperMonstre(map,superMonstre,jmin,perso):
    #génère les superMonstres à des coordonnées aléatoire en vérifiant qu'il y est une plateforme en dessous de lui 
    #ajoute les coordonnées dans la liste de superMonstres 
    #renvoie la liste 
    while True:
        x=randint(0,39)
        a=jmin-27
        b=(perso[1]//30)-6
        y=randint(a,b)
        if map[y][x] == "x":
            superMonstre.append((x,y-1))
            return (superMonstre)

