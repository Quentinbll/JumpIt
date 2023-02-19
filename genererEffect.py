from random import randint

def genererEffect(map,posEffect,jmin,perso):
    while True:
        x=randint(0,39)
        a=jmin-27
        b=(perso[1]//30)-6
        y=randint(a,b)
        if map[y][x] == "x":
            posEffect.append((x,y-1))
            return (posEffect)