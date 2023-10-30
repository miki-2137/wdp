def rownanie():
    print('ax+b=0')
    a = float(input('podaj liczbe a: '))
    b = float(input('podaj liczbe b: '))
    if a == 0:
        print('rownanie nie ma rozwiazania')
    else:
        x = -b/a
        return x
print('x =', rownanie())