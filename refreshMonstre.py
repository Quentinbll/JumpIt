def refreshMonstres(monstres,superMonstre,jmin,nbmonstres,nbsmonstres):
    #enlève les monstres de la liste se retrouvant en dessous de la map
    #idem pour les superMonstre
    #renvoie les liste et le nombre de monstre restant
    for m in superMonstre:
        if m[1]>jmin+28:
            superMonstre.remove(m)
            nbsmonstres=nbsmonstres-1
    
    for m in monstres:
        if m[1]>jmin+28:
            monstres.remove(m)
            nbmonstres=nbmonstres-1
    
    return (monstres,superMonstre,nbmonstres,nbsmonstres)
