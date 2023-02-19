def refreshEffect(posEffect, jmin,nbeffect):

    for e in posEffect:
        if e[1]>jmin+28:
            posEffect.remove(e)
            nbeffect=nbeffect-1
        

    return (posEffect,nbeffect)
