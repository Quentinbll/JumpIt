def afficherMonstres(fenetre,superMonstre,monstres,jmin,imageMonstres):
    #affiche les monstres en parcourant la liste 
    m=-1
    for i in monstres:
        m=m+1
        xm=monstres[m][0]*30
        ym=monstres[m][1]*30-(jmin*30)+12
        fenetre.blit(imageMonstres[0], (xm,ym))
    sm=-1
    for i in superMonstre:
        sm=sm+1
        xsm=superMonstre[sm][0]*30
        ysm=superMonstre[sm][1]*30-(jmin*30)
        fenetre.blit(imageMonstres[1], (xsm,ysm))