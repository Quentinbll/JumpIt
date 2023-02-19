def afficherPersonnage(fenetre, perso, jmin, imagePerso ):
    #affiche le personnage aux coordonées données
    y = perso[1]-(jmin*30)+2
    fenetre.blit(imagePerso, (perso[0], y))
