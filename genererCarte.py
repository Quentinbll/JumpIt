def genererCarte():
    #ouvre le fichier map 
    #tranforme en liste la map
    #renvoie map 
    with open("(texte)map.txt","r") as fichier :
        map = fichier.read()
    map = map.split("\n")

    for i in range (len(map)):
        map[i]=list(map[i])
    return map




