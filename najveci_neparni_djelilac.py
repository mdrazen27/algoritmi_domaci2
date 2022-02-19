def djelilac(n):
    """
    Napisati metod int djelilac(int n) koji vraća najveći neparni pozitivni djelilac broja n. 
    """
    if n<=0:
        return "nepravilan unos"
    max=1
    for i in range(1,n+1,2):
        if n%i==0:
            max=i
        elif n/i<2:
            if n%2 != 0:
                return n
            else:
                break
    return max

print(djelilac(int(input("unesite broj n: "))))