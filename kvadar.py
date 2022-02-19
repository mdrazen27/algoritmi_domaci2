def p_v_kvadara(a,b,c):
    """
    Napisati kod koji za date stranice a, b i c kvadra računa površinu 
    i zapreminu kvadra..
    """
    p = 2*(a*b + a*c + b*c)
    v = a*b*c
    print("Povrsina je:",p)
    print("Zapremina je:",v)
a = int(input("Unesite stranicu a: "))
b = int(input("Unesite stranicu b: "))
c = int(input("Unesite stranicu c: "))

p_v_kvadara(a,b,c)
