def zbir_min_max_cif(n):
    """
    Napisati metod int minMaxCifra(int n) koji vraća zbir najveće i najmanje cifre broja n 
    """
    zbir = 0
    max = min = n%10
    while n:
        k = n%10
        if k < min:
            min = k 
        if k > max:
            max = k
        n //= 10
    return min+max

print(zbir_min_max_cif(int(input("Unesite pozitivan broj n: "))))