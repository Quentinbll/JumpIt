def acceleration(v, direction):
    #augmente ou diminue la vitesse de deplacement sur l'axe horizontale en fonction du déplacement
    if direction == 1 :
        v = (max(-5, v[0] - 1), v[1])
    elif direction == -1 : 
        v = (min(5, v[0] + 1), v[1])
    else:
        v = (int(v[0] / 2), v[1])
    return v
        