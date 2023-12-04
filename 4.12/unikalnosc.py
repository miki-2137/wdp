lista = [8,5,8,2,5,3,8,7]

def unikalnosc(lista):
    u = []
    for i in lista:
        if i not in u: #if not czy_nalezy(u,i)
            u.append(i)
    return u

print(unikalnosc(lista))

def czestosc(lista):
    d = {}
    for i in lista:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    return d

print(czestosc(lista))