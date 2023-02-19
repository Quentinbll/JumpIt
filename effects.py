from random import randint

def effect(perso, effect, listEffect, nbEffect):

    for e in effect:
        x = perso[0]
        y = perso[1]
        xe=e[0]*30
        ye=e[1]*30
        for i in range(x-18,(x+12)):
            if i==xe:
                for i1 in range(y,(y+10)):
                    if i1==ye:
                        a= randint(0,1)
                        print(listEffect[a])
                        effect.remove(e)
                        nbEffect = nbEffect-1    
                        return listEffect[a], nbEffect
    return None, nbEffect