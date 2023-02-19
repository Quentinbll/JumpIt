import pygame
from random import *
def tirfonction(perso,souris, map,jmin, superMonstre,monstres,imageBackground):
    pos_spmonstre=[]
    vecteur_spmonstre=[]
    touché_spm=[]
    z_spm=[]
    disparition_spm=[]
    pos_perso=perso[0]+15,perso[1]-jmin*30+15
    pos_monstre=[]
    vecteur_monstre=[]
    touché_m=[]
    z_m=[]
    disparition_m=[]
    for i in range(len(superMonstre)):
        pos_spmonstre.append((superMonstre[i][0]*30+15,superMonstre[i][1]*30-jmin*30+15))
        vecteur_spmonstre.append((pos_spmonstre[i][0]-pos_perso[0],pos_spmonstre[i][1]-pos_perso[1]))
        touché_spm.append(False)
        disparition_spm.append(False)
    for i in range(len(monstres)):
        pos_monstre.append((monstres[i][0]*30+15,monstres[i][1]*30-jmin*30+15))
        vecteur_monstre.append((pos_monstre[i][0]-pos_perso[0],pos_monstre[i][1]-pos_perso[1]))
        touché_m.append(False)
        disparition_m.append(False)
        
    color=255,0,0,255
    vecteur_line=souris[0]-pos_perso[0],souris[1]-pos_perso[1]
    
    
    a=vecteur_line[0]
    b=-vecteur_line[1]
    m=-b/a
    p=souris[1]-m*souris[0]
    if a>0:
        end_pos=1200,m*1200+p
        for x in range(1199,pos_perso[0],-1):
            if map[min(99999,max(0,int((m*x+p))//30+jmin))][x//30]=='x':
                end_pos=x,m*x+p
        
    else:
        end_pos=0,p
        for x in range(0,pos_perso[0],+1):
            if map[min(99999,max(0,int((m*x+p))//30+jmin))][x//30]=='x':
                end_pos=x,m*x+p
    for i in range(len(superMonstre)):
        if ((end_pos[0]-pos_perso[0])**2+(end_pos[1]-pos_perso[1])**2)**0.5>((pos_spmonstre[i][0]-pos_perso[0])**2+(pos_spmonstre[i][1]-pos_perso[1])**2)**0.5:
            touché_spm[i]=True
        z_spm.append(m*pos_spmonstre[i][0]+p-pos_spmonstre[i][1])
        if ((z_spm[i]>-20 and z_spm[i]<20) and ((a>0 and vecteur_spmonstre[i][0]>0) or (a<0 and vecteur_spmonstre[i][0]<0))) and ((b>0 and -vecteur_spmonstre[i][1]>0) or (b<0 and -vecteur_spmonstre[i][1]<0)) and touché_spm[i]:
            disparition_spm[i]=True
    for i in range(len(monstres)):
        if ((end_pos[0]-pos_perso[0])**2+(end_pos[1]-pos_perso[1])**2)**0.5>((pos_monstre[i][0]-pos_perso[0])**2+(pos_monstre[i][1]-pos_perso[1])**2)**0.5:
            touché_m[i]=True
        z_m.append(m*pos_monstre[i][0]+p-pos_monstre[i][1])
        if ((z_m[i]>-20 and z_m[i]<20) and ((a>0 and vecteur_monstre[i][0]>0) or (a<0 and vecteur_monstre[i][0]<0))) and ((b>0 and -vecteur_monstre[i][1]>0) or (b<0 and -vecteur_monstre[i][1]<0)) and touché_m[i]:
            disparition_m[i]=True
    pygame.draw.line(imageBackground,color, pos_perso, end_pos,3)
    
    return disparition_m,disparition_spm