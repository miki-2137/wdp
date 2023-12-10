zdanie = 'Ala ma kota.'


def slownik(zdanie):
    d = {}
    for i in zdanie:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    return d

def litery(slownik):
    d = {}
    for k in slownik:
        k=k.lower()
        if k.isalpha():
            d[k]=slownik[k]
    return d

print(litery(slownik(zdanie)))