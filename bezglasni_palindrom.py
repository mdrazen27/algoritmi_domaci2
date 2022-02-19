def bezglasni_palindrom(s):
    """
    Dozvoljena je sljedeća operacija: u riječi uzmemo prvi suglasnik i zamijenimo mjesta sa
    posljednjim suglasnikom; drugi suglasnik zamijeni mjesta sa pretposljednjim suglasnikom, itd. Ako
    poslije te operacije opet dobijemo polaznu riječ, tada takvu riječ nazivamo bezglasni palindrom (npr.
    takve su riječi sos, rare, rotor, gong, karaoke). Napisati program koji provjerava da li je data riječ
    bezglasni palindrom. Ulaz: Unosi se jedna riječ, dužine ne veće od 20, samo mala slova. Izlaz:
    Štampati YES ili NO, 
    tennete YES
    karaoke YES
    disk NO 
    """
    k=[]
    s=list(s)
    samoglasnici = ['a','e','i','o','u']
    for i in s:
        if i not in samoglasnici:
            k.append(i)
    if k == k[::-1]:
        return print ("YES")
    return print("NO")
bezglasni_palindrom(input("unesite rijec za provjeru: "))