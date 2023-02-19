
import pygame
import sys
def demanderNom():   
    #demande le pseudo de l'utilisateur 
    #le pseudo peut etre composé des lettres de l'alphabet(maj et min), de chiffres et d'espaces
    #le nom est renvoyé 
    pygame.font.init()
    fenetre = pygame.display.set_mode((1200, 1040))
    imageFond = pygame.image.load("AAAFond.png")
    
    police = pygame.font.SysFont(" ", 80)
    listeCaractere = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','0', '1', '2', '3',
    '4', '5', '6', '7', '8', '9',' ']
    consigne = "Entrez Votre Pseudo :"
    afficherConsigne = police.render(consigne, True, (0,0,0))
    nom = ""
    text = police.render(nom, True, (0,0,0))
    run = True
    while run:
        nomMaj = nom.upper()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    nom = nom[:-1]
                    nomMaj = nomMaj[:-1]
                    text = police.render(nomMaj, True,  (0,0,0))
                if (event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER) and len(nomMaj) > 0:   
                    run = False
                                  
            if event.type == pygame.TEXTINPUT:
                if event.text in listeCaractere:
                    nom += event.text
                    nomMaj = nom.upper()
                    text = police.render(nomMaj, True,  (0,0,0))
            

        fenetre.blit(imageFond, (0,0))
        fenetre.blit(text, (450, 570))
        fenetre.blit(afficherConsigne, (340, 460))
        pygame.display.update()
    
    return nomMaj
    



    