def afficherScore(fenetre,score,police, nom):
    #affiche le nom et le score de l'utilisateur aux coordonnées données
    nom = police.render("PSEUDO : " + nom , False, (0,0,0)) 
    score = police.render("VOTRE SCORE : " + str(score), False, (0,0,0))
    fenetre.blit(score, (1070,125))
    fenetre.blit(nom, (1070,110))
    