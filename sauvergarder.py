
def sauvergarder(niveau , nom, score):
    #lis le ficher des records en fonction du niveau en extrait une liste
    #regarde si le nom de l'utilisateur est déja dans la liste, si c'est le cas remplace le score dans le cas où il est plus élevé
    #sinon réécris chaque liste jusqu'à l'avant dernière puis écris la derniere avec le nom de l'utilisateur et son score 

    if niveau == "1":
        listeRecord = "(texte)recordFacile.csv"
    elif niveau == "2":
        listeRecord = "(texte)recordMoyen.csv"
    elif niveau == "3":
        listeRecord = "(texte)recordDifficile.csv"
    elif niveau == "4":
        listeRecord = "(texte)recordImpossible.csv"
    
    with open(listeRecord, "r") as file:
        record = file.read()
        record =record.split("\n")
        for i in range(len(record)):
            record[i] =record[i].split(" ")
        for i in range(len(record)):
            record[i][1]= int(record[i][1])
            
        record.sort(key=lambda element: element[1], reverse=True)
        a = False
        b = False
        p= 1
        for i in range(len(record)):
            if nom in record[i][0] and score > record[i][1]:
                record[i] = [nom,str(score)]
                recordStr = " ".join(record[i])
                b = True
                
                
    with open(listeRecord, "w") as file:  
        if b == True:
             for line in record:
                if line == record[4]:
                    file.write(line[0]+" "+ str(line[1]))
                else:
                    file.write(line[0]+" "+ str(line[1])+"\n")
                
        else:
            for line in record:
                if p != 5:
                    file.write(line[0] +" "+ str(line[1])+ "\n")
                    p=p+1
                elif p == 5:
                    if nom not in record[0][0] and nom not in record[1][0] and nom not in record[2][0] and nom not in record[3][0] and nom not in record[4][0] :
                        file.write(nom + " "+ str(score))
                        a = True
                    elif a == False :
                        file.write(record[-1][0] + " " +str(record[-1][1]))
    

       
