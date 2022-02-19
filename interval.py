def najmanji_interval(a,b,c,d):
    """
    Napisati metod double unijaIntervala(double a, double b, double c,
    double d) koji vraća dužinu najmanjeg intervala koji sadrži i [a,b] i [c,d], a<=b,
    c<=d. 
    """
    if a<= c:
        if b<=d:
            return f'[ {a} , {d} ]'
        else:
            return f'[ {a} , {b} ]'
    else:
        if b<=d:  
            return f'[ {c} , {d} ]'
        else:
            return f'[ {c} , {b} ]'

a = float(input("Uniesite a: "))
b = float(input("Uniesite b: "))
c = float(input("Uniesite c: "))
d = float(input("Uniesite d: "))
print("najmanji interval je:",najmanji_interval(a,b,c,d))
    