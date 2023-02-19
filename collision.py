def collision(map, perso, v):
    #regarde pour chaque direction si le personnage va rentrer en collision avec une plateforme 
    #si c'est le cas elle met la vitesse du personnage à 0 dans la direction où il allait 
    x = (perso[0]+v[0])//30
    y = (perso[1]+v[1])//30
    if x<0:
        x=0
    elif x>38:
        x=38
    if v[0]>0 :
        if map[perso[1]//30][x+1] == "x" or map[perso[1]//30+1][x+1] == "x" :
            v = (0,v[1])
    if v[0]<0 : 
        if map[perso[1]//30][x-1] == "x" or map[perso[1]//30+1][x-1] == "x" :
            v = (0,v[1])
    if v[1]>0 :
        if map[y+1][x] == "x" or map[y+1][x+1] == "x":
            v = (v[0], 0)
    if v[1]<0 : 
        if map[y][x] == "x" or map[y][x+1] == "x":
            v = (v[0], 0)
    return v 