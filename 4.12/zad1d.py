zdanie = 'Ala ma kota.'


def slownik(zdanie):
    d = {}
    for i in zdanie:
        if not i.isalpha():
            continue
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    return d

print(slownik(zdanie))

def min_d(d):
    key_min = next(iter(d))
    for i in d:
        if d[i] < d[key_min]:
            key_min = i
    return key_min

print (min_d(slownik(zdanie)))

def max_d(d):
    key_max = next(iter(d))
    for i in d:
        if d[i] > d[key_max]:
            key_max = i
    return key_max

print (max_d(slownik(zdanie)))
