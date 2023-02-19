def afficherRecord(record, police, fenetre):
    #affiche le record au coordonnée donnée
    coordonné = (1050,5)
    for i in range(len(record)):   
        classement = i+1
        afficherRecord = police.render(str(classement) +": "+ record[i][0]+ ": "+ str(record[i][1]) , False, (0,0,0))
        fenetre.blit(afficherRecord, coordonné)
        coordonné = (coordonné[0],coordonné[1]+20)
    
    
