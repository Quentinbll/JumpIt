def disparition(disparition_m,disparition_spm,monstres,superMonstre,score,smmort,nbmonstres,nbsmonstres,effect):
    i=-1
    for m in disparition_m:
        i=i+1
        if m == True:
            monstres.pop(i)
            nbmonstres=nbmonstres-1
            if effect == "coin*2":
                score=score+2
            else:
                score=score+1
    i=-1
    for m in disparition_spm:
        i=i+1
        if m==True:
            smmort[i]=smmort[i]+1
        if smmort[i]==3:
            superMonstre.pop(i)
            nbsmonstres=nbsmonstres-1
            if effect == "coin*2":
                score=score+4
            else:
                score = score+2
            smmort[i]=0
    return monstres,superMonstre,score,smmort,nbmonstres,nbsmonstres
    
