    
import pygame
import sys
def choixNiveau():
    #demande a l'utilisateur de choisir un niveau parmis 4
    #la fonction renvoie le niveau choisi
    
    pygame.font.init()
    fenetre = pygame.display.set_mode((1200, 1040))
    imageFond = pygame.image.load("AAAFond.png")
    
    
    police = pygame.font.SysFont(" ", 80)
    listeCaractere = ["1","2","3","4"]
    consigne = "Choissisez un niveau:"
    niveau1 = "1: Facile"
    niveau2 = "2: Moyen"
    niveau3 = "3: Difficile"
    niveau4 = "4: Impossible"
    afficherConsigne = police.render(consigne, True, (0,0,0))
    afficherNiveau1 = police.render(niveau1,True, (0,0,0))
    afficherNiveau2 = police.render(niveau2,True, (0,0,0))
    afficherNiveau3 = police.render(niveau3,True, (0,0,0))
    afficherNiveau4 = police.render(niveau4,True, (0,0,0))
    choixNiveau = ""
    text = police.render(choixNiveau, True, (0,0,0))
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    choixNiveau = choixNiveau[:-1]
                    text = police.render(choixNiveau, True,  (0,0,0))
                if (event.key == pygame.K_RETURN  or event.key == pygame.K_KP_ENTER) and len(choixNiveau) == 1:   
                    run = False
                                  
            if event.type == pygame.TEXTINPUT:
                if event.text in listeCaractere and len(choixNiveau) < 1:
                    choixNiveau += event.text
                    text = police.render(choixNiveau, True,  (0,0,0))
            
    
        fenetre.blit(imageFond, (0, 0))
        fenetre.blit(text, (590, 520))
        fenetre.blit(afficherConsigne, (300, 560))
        fenetre.blit(afficherNiveau1, (300, 160))
        fenetre.blit(afficherNiveau2, (300, 240))
        fenetre.blit(afficherNiveau3, (300, 320))
        fenetre.blit(afficherNiveau4, (300, 400))
        pygame.display.update()
    
    return choixNiveau 



    