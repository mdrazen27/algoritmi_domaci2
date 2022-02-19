def uklanjanje_razmaka(s):
    """
    U datom stringu sve uzastopne blankove (ako ih ima više od jednog) zamijeniti jednim
    blankom.    
    """
    k = []
    s = s.split(" ")
    for i in s:
        if i != '':
            k.append(i)
    return ' '.join(k)

print('sa uklonjenim razmacima je:',uklanjanje_razmaka(input("unesite recenicu iz koje trebaju da se uklone suvisni razmaci: "))) 