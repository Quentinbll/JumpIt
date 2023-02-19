import pygame
def afficherTimerEffect(effect, imageEffect, fenetre, effectTime):
    timerText = 20       
    if effect == "jumpBoost" and effectTime is not None :
        fenetre.blit(imageEffect[1], (10,10))
        timerPolice = pygame.font.Font("police.ttf", 30)
        timerText = str(effectTime)
        timer = timerPolice.render(timerText, True, (0,0,0))
        fenetre.blit(timer,(40,10))
    if effect == "coin*2" and effectTime is not None:
        fenetre.blit(imageEffect[2], (10,10))
        timerPolice = pygame.font.Font("police.ttf", 30)
        timerText = str(effectTime)
        timer = timerPolice.render(timerText, True, (0,0,0))
        fenetre.blit(timer,(40,10))
    
    
        
            

            
        
    
    
     