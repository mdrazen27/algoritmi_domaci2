"""
Napisati metod int nadjiNajveciTrougao(int n) koji sa standardnog ulaza (pomoću
klase Scanner) učitava n trojki pozitivnih cijelih brojeva (a, b, c) i vraća površinu najvećeg
trougla sa stranicama a, b i c. Napomena: Napišite metod koji računa površinu trougla i koristite
ga u metodu nadjiNajveciTrougao.
"""
import math
def povrsina_trougla(a,b,c):
    s = (a+b+c)/2
    k = s*(s-a)*(s-b)*(s-c)
    if k >= 0:
        return  math.sqrt(k)
    return 0

def najveci_trougao(n):
    max=0
    for i in range(n):
        a = float(input("Unesite stranicu a: "))
        b = float(input("Unesite stranicu b: "))
        c = float(input("Unesite stranicu c: "))
        if povrsina_trougla(a,b,c)> max:
            max = povrsina_trougla(a,b,c)
    return max

print(najveci_trougao(int(input("unesite broj trouglova za poredjenje: "))))
