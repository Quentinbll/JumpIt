import pygame
import sys 

def rejouer(police, fenetre, score):
    #a la fin de la partie demande à l'utilisateur s'il veut rejouer 
    #si oui : renvoie reponse = True
    #si non : renvoie reponse = False
    pygame.init()
    pygame.font.init()
    fenetre = pygame.display.set_mode((1200, 1040))
    imageFond = pygame.image.load("AAAFond.png")
    consigne = "Voulez vous rejouer ? (O/N) :"
    afficherConsigne = police.render(consigne, True, (0,0,0))
    reponse = ""
    text = police.render(reponse, True, (0,0,0))
    partiePerdu = "Game Over"
    afficherPartiePerdu = police.render(partiePerdu, True, (0,0,0))
    strScore = "Votre score : " + str(score)
    afficherScore =  police.render(strScore, True, (0,0,0))
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    reponse = reponse[:-1]
                    text = police.render(reponse, True,  (0,0,0))
                if (event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER) and len(reponse) ==1 :   
                    run = False
                                  
            if event.type == pygame.TEXTINPUT:
                if (event.text == "o" or event.text == "O" or event.text == "y" or event.text == "Y" or event.text == "n" or event.text == "N") and len(reponse) == 0:
                    reponse += event.text
                    text = police.render(reponse, True,  (0,0,0))
            

        fenetre.blit(imageFond, (0,0))
        fenetre.blit(text, (590, 620))
        fenetre.blit(afficherPartiePerdu, (490,200))
        fenetre.blit(afficherConsigne, (300, 560))
        fenetre.blit(afficherScore, (450,300))
        pygame.display.update()
    return reponse

