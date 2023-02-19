def monstre(perso, monstres, superMonstre, run):
    #regarde si les coordonnées du personnage sont les mêmes que celle d'un monstre si c'est le cas renvoie run = false 
    #Idem pour les superMonstres
    for m in monstres:
        x = perso[0]
        y = perso[1]
        xm=m[0]*30
        ym=m[1]*30
        for i in range(x-18,(x+12)):
            if i==xm:
                for i1 in range(y,(y+10)):
                    if i1==ym:
                        run=False
                        return run
    for m in superMonstre:
        xm=m[0]*30
        ym=m[1]*30
        for i in range(x-18,(x+12)):
            if i==xm:
                for i1 in range(y,(y+10)):
                    if i1==ym:
                        run=False
                        return run
    return run