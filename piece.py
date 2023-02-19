import pygame
def piece(map,perso, score, effect,soundEffect):
    #regarde si les coordonnées du personnage sont les même que celle d'une pièce, si c'est le cas remplace "p" par "o" dans la map et ajoute 1 au score
    x = perso[0] // 30
    y = perso[1] // 30
    if x<0:
        x=0
    elif x>38:
        x=38
    if map[y][x] == "p" :
        pygame.mixer.Sound.play(soundEffect[1])
        map[y][x] = "o"
        if effect == "coin*2":
            score += 2
        else:
            score += 1 
    if map[y][x+1] =="p" :
        pygame.mixer.Sound.play(soundEffect[1])
        map[y][x+1] = "o"
        if effect == "coin*2":
            score += 2
        else:
            score += 1 
    if map[y+1][x] == "p" :
        pygame.mixer.Sound.play(soundEffect[1])
        map[y+1][x] = "o"
        if effect == "coin*2":
            score += 2
        else:
            score += 1 

    return map , score

