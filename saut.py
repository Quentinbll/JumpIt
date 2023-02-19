import pygame

def saut(map, perso, v, soundEffect, effect): 
    #si les coordonnées du personnage sont au dessus d'une plateforme il peut "sauter"
    #"sauter" siginifie mettre sa vitesse verticale à -30 
    # renvoie v 
    x = perso[0]//30
    if map[(perso[1]+10)//30+1][x] == "x" or map[(perso[1]+10)//30+1][x+1] == "x":
        if effect == "jumpBoost":
            v = (v[0], -45)
        else:
            v = (v[0], -30)
        pygame.mixer.Sound.play(soundEffect[0])
        
    return v