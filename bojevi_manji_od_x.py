def brojevi_manji_od_x(x):
    """
    koji učitava cijele brojeve, sve dok se ne učita
    cio broj koji je veći od x, a zatim štampa broj učitanih brojeva, broj učitanih parnih brojeva i
    zbir svih učitanih brojeva. 
    """
    k= 0
    br_ucitanih = 0 
    br_parnih = 0 
    zbir_svih = 0 
    while k <= x:
        k= int(input("Unesite cio broj: "))
        if k%2 == 0:
            br_parnih += 1
        br_ucitanih += 1
        zbir_svih += k
    return f'broj ucitanih brojeva je {br_ucitanih},broj parnih brojeva je {br_parnih}, zbir svih brojeva je {zbir_svih}' 

print(brojevi_manji_od_x(int(input("Unesite broj x: "))))   
