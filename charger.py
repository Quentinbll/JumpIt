def charger(niveau):
    #Ouvre le fichier des records en fonction du niveau donné
    #Transforme le str en liste puis le trie 
    #La nouvelle liste est renvoyé
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
   
        
    return record






         