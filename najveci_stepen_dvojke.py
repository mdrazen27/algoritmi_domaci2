def stepen_dvojke(n):
    """Napisati metod int minStepenDvojke(int n) koji vraća najmanji prirodan broj k
    takav da n nije veći od broja 2^k. 
    """
    k = 0 
    while 2**k < n:
        k += 1
    return k

print('k =',stepen_dvojke(int(input("unesite broj n: "))))
