def afficherLave(fenetre, imageCarte):
    #affiche la lave 
    x=-30
    for i in range(40):
        x=x+30
        fenetre.blit(imageCarte[3], (x,990))