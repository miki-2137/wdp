def plik(plik):
    l = []
    o = open(plik)
    r = o.readlines()
    for char in r:
        for k in char:
            if k.isalpha():
                l.append(k)
    return l

def slownik(lista):
    d = {}
    for i in lista:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    return d

print(slownik(plik('test.txt')))
