def afficherCarte(map,jmin,imageCarte,fenetre, background):
    #affiche la carte en regardant pour chaques éléments de map :
    # si o = ciel(rien afficher car fond)
    # si x = plateforme 
    # si p = pièce  
    x = 0
    y = 0
    fenetre.blit(background, (x,y))
    mapafficher=[]
    for i in range (jmin,jmin+36):
        mapafficher.append(map[i])

    for i in mapafficher:
        for case in i : 
            if case == "o" : 
                x=x+30
            elif case == "p":
                fenetre.blit(imageCarte[0], (x,y))
                x=x+30
            elif case == "x": 
                fenetre.blit(imageCarte[1],(x,y))
                x=x+30
        x = 0
        y=y+30