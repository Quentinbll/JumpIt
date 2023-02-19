import pygame
import sys
import genererCarte
import afficherCarte
import afficherPersonnage
import acceleration
import deplacement
import saut
import genererMonstre
import genererSuperMonstre
import refreshMonstre
import afficherMonstre
import collision
import piece
import afficherScore
import demanderNom
import charger
import sauvergarder
import afficherRecord
import rejouer
import monstre
import choixNiveau
import afficherLave
import genererEffect
import effects
import refreshEffect
import afficherEffect
import afficherTimerEffect
import tirAfficher
import disparition

def main():
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()
    nom = demanderNom.demanderNom()
    niveau = choixNiveau.choixNiveau()
    horlogeMap = pygame.USEREVENT +1
    if niveau == "1":
        pygame.time.set_timer(horlogeMap, 1000)
    elif niveau == "2":
        pygame.time.set_timer(horlogeMap, 450)
    elif niveau == "3":
        pygame.time.set_timer(horlogeMap, 300)
    elif niveau == "4":
        pygame.time.set_timer(horlogeMap,200)
    horloge = pygame.USEREVENT +2
    pygame.time.set_timer(horloge, 50) 
    
    fenetre = pygame.display.set_mode((1200,1040))
    imageBackground = pygame.image.load("AAAbackgroundGame.jpg")
    imageCarte = [pygame.image.load("AAApiece.png"),pygame.image.load("AAAplateforme.png"),pygame.image.load("AAAciel.png"),pygame.image.load("AAAlave.png")]
    imagePerso = pygame.image.load("AAAhero.png")
    imageMonstre = [pygame.image.load("AAAmonstre.png"),pygame.image.load("AAASMonstre.png")]
    imageEffect =  [pygame.image.load("AAAeffect.png"), pygame.image.load("AAAjumpBoost.png"),pygame.image.load("AAAcoinBonus.png")]
    soundEffect = [pygame.mixer.Sound("jump.ogg"),pygame.mixer.Sound("Coin.ogg"),pygame.mixer.Sound("Laser-weapon.ogg")]
    map=genererCarte.genererCarte()
    record = charger.charger(niveau)
    jmin=99964
    perso =  [510,2999480]
    monstres=[]
    superMonstre=[]
    listEffect = ["jumpBoost", "coin*2"]
    posEffect = []
    nbEffect = 2
    effect = None
    effectTime = 20
    tir = True
    smmort = [int(0),int(0),int(0),int(0)]
    

    if niveau == "1":
        nbmonstres=2
        nbsmonstres=1
        for i in range(2):
            monstres=genererMonstre.genererMonstres(map,monstres,jmin,perso)
        for i in range(1):
            superMonstre=genererSuperMonstre.genererSuperMonstre(map,superMonstre,jmin,perso)
    elif niveau == "2":
        nbmonstres=5
        nbsmonstres=2
        for i in range(5):
            monstres=genererMonstre.genererMonstres(map,monstres,jmin,perso)
        for i in range(2):
            superMonstre=genererSuperMonstre.genererSuperMonstre(map,superMonstre,jmin,perso)
    elif niveau == "3":
        nbmonstres=10
        nbsmonstres=4
        for i in range(10):
            monstres=genererMonstre.genererMonstres(map,monstres,jmin,perso)

            
        for i in range(4):
            superMonstre=genererSuperMonstre.genererSuperMonstre(map,superMonstre,jmin,perso)
    elif niveau == "4":
        nbmonstres=10
        nbsmonstres=4
        for i in range(10):
            monstres=genererMonstre.genererMonstres(map,monstres,jmin,perso)
        for i in range(4):
            superMonstre=genererSuperMonstre.genererSuperMonstre(map,superMonstre,jmin,perso)
            
    for i in range(2):
        posEffect = genererEffect.genererEffect(map,posEffect,jmin,perso)
    G = 2
    score = 0
    qPressed = False
    dPressed = False
    v = (0,0)
    police = pygame.font.Font("police.ttf",11)
    run=True
    start = False
    while run:
        fenetre.fill((0,0,0))  
        afficherCarte.afficherCarte(map, jmin, imageCarte, fenetre, imageBackground)
        afficherPersonnage.afficherPersonnage(fenetre, perso, jmin, imagePerso )
        afficherMonstre.afficherMonstres(fenetre,superMonstre,monstres,jmin,imageMonstre)
        afficherScore.afficherScore(fenetre, score, police, nom)
        afficherRecord.afficherRecord(record,police,fenetre)
        afficherLave.afficherLave(fenetre, imageCarte)
        afficherEffect.afficherEffect(fenetre,posEffect,jmin,imageEffect)
        afficherTimerEffect.afficherTimerEffect(effect, imageEffect, fenetre, effectTime)
        pygame.display.flip() 
    
                
        for event in pygame.event.get():    
            if event.type == pygame.QUIT: 
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and tir==True:
                    souris=pygame.mouse.get_pos()
                    disparition_m,disparition_spm=tirAfficher.tirfonction(perso,souris, map,jmin, superMonstre, monstres, imageBackground)
                    monstres,superMonstre,score,smmort,nbmonstres,nbsmonstres=disparition.disparition(disparition_m,disparition_spm,monstres,superMonstre,score,smmort,nbmonstres,nbsmonstres,effect)
                    tir=False  
            if event.type == pygame.KEYDOWN:
                start = True
                if event.key == pygame.K_q:
                    qPressed = True
                if event.key == pygame.K_d:
                    dPressed = True
                if event.key == pygame.K_SPACE:
                    v = saut.saut(map, perso, v, soundEffect, effect)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_q:
                    qPressed = False
                if event.key == pygame.K_d:
                    dPressed = False  

            if event.type == horlogeMap and start or jmin +5 > perso[1]//30:
                jmin=jmin-1
                imageBackground.fill((0,0,0))
                imageBackground = pygame.image.load("AAAbackgroundGame.jpg")
                tir = True
                                    
            if event.type == horloge and start:
                if qPressed :
                    v = acceleration.acceleration(v,1)
                elif dPressed : 
                    v = acceleration.acceleration(v,-1)
                else :
                    v = acceleration.acceleration(v, 0)
                v =(v[0],min(20,v[1]+G))
                    
                v=collision.collision(map, perso, v)
                perso = deplacement.deplacement(perso,v)
               
            if event.type == horlogeMap and effect is not None:
                effectTime = effectTime - 1    
            
            if effectTime < 0:
                effect = None
                effectTime = 20
            
            
        
        posEffect, nbEffect = refreshEffect.refreshEffect(posEffect,jmin, nbEffect)
        while nbEffect != 2:
            posEffect= genererEffect.genererEffect(map,posEffect,jmin,perso)
            nbEffect =nbEffect+1
        if effect is None:    
            effect, nbEffect = effects.effect(perso, posEffect, listEffect, nbEffect)
        
        monstres, superMonstre, nbmonstres,nbsmonstres=refreshMonstre.refreshMonstres(monstres,superMonstre,jmin,nbmonstres,nbsmonstres)
        map, score = piece.piece(map, perso, score, effect,soundEffect)
        run = monstre.monstre(perso,monstres, superMonstre, run)
        if niveau == "1":
            while nbmonstres!=2:
                monstres=genererMonstre.genererMonstres(map,monstres,jmin,perso)
                nbmonstres=nbmonstres+1
            while nbsmonstres!=1:
                superMonstre=genererSuperMonstre.genererSuperMonstre(map,superMonstre,jmin,perso)
                nbsmonstres=nbsmonstres+1
        elif niveau == "2":
            while nbmonstres!=5:
                monstres=genererMonstre.genererMonstres(map,monstres,jmin,perso)
                nbmonstres=nbmonstres+1
            while nbsmonstres!=2:
                superMonstre=genererSuperMonstre.genererSuperMonstre(map,superMonstre,jmin,perso)
                nbsmonstres=nbsmonstres+1
        elif niveau == "3":
            while nbmonstres!=10:
                monstres=genererMonstre.genererMonstres(map,monstres,jmin,perso)
                nbmonstres=nbmonstres+1
            while nbsmonstres!=4:
                superMonstre=genererSuperMonstre.genererSuperMonstre(map,superMonstre,jmin,perso)
                nbsmonstres=nbsmonstres+1
        elif niveau == "4":
            while nbmonstres!=10:
                monstres=genererMonstre.genererMonstres(map,monstres,jmin,perso)
                nbmonstres=nbmonstres+1
            while nbsmonstres!=4:
                superMonstre=genererSuperMonstre.genererSuperMonstre(map,superMonstre,jmin,perso)
                nbsmonstres=nbsmonstres+1      
        
        if jmin==1 or jmin+33 == perso[1]//30 or perso[1]//30 == 99999:
            pygame.quit()
            run = False
        

    if score > record[-1][1]: 
        sauvergarder.sauvergarder(niveau, nom, score)
    pygame.init()
    pygame.font.init()
    reponse = rejouer.rejouer(pygame.font.SysFont("", 60), pygame.display.set_mode((1200,1040)), score)
    if reponse == "o" or reponse == "O" or reponse == "y" or reponse == "Y":
        main()
    else:
        pygame.quit()
        sys.exit()
    
main()