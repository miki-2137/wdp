def plik(plik):
    l = []
    try:
        o = open(plik)
    except:
        print("Nie ma takiego pliku")
    while True:
        r = o.readline()
        if len(r) == 0:
            break
        s = r.split()
        for i in s:
            if i.isnumeric():
                l.append(i)
    o.close()
    return l

def slownik(lista):
    d = {}
    for i in lista:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    return d

print(slownik(plik('test2.txt')))

-------------------------------------
def program(sciezka):
    d = {}
    with open(sciezka,'r') as plik:
        for linia in plik:
            elementy = linia.split()
            for element in elementy:
                try:
                    element = int(element)
                    if element in d:
                        d[element] =+ 1
                    else:
                        d[element] = 1
                except:
                    pass
    return d


print(program('test.txt'))
