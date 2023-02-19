def deplacement(perso, v):
    #modifie les coordonnées du personnage avec le vecteur de son déplacement
    #renvoie les nouvelles coordonnées
    perso = [perso[0]+ v[0], perso[1]+v[1]]
    if perso[0]>1169:
        perso[0]=1169
    elif perso[0]<1:
        perso[0]=1
    
    return perso


    