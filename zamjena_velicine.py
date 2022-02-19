def zamjena_velicine(s):
    """
    Promijeniti „veličinu“ simbola: ako je malo slovo pretvoriti
    ga u veliko i obratno
    """
    if s.upper() == s:
        return s.lower()
    return s.upper()

print(zamjena_velicine(input("Unesite karakter: ")))
