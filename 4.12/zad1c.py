zdanie = 'Ala ma kota.'


def slownik(zdanie):
    d = {}
    for i in zdanie:
        if not i.isalpha():
            continue
        i = i.lower()
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    return d

print(slownik(zdanie))
