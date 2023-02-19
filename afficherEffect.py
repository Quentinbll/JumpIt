def afficherEffect(fenetre,poseffect,jmin,imageEffect):
    e=-1
    for i in poseffect:
        e=e+1
        xe=poseffect[e][0]*30
        ye=poseffect[e][1]*30-(jmin*30)
        fenetre.blit(imageEffect[0], (xe,ye))
