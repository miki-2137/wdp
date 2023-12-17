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

print(plik('test2.txt'))
