# d={} - slownik

d={5:3,8:4}
print(d[5])

zdanie = 'Ala ma kota.'

def czy_nalezy(lista,n):
    for i in lista:
        if n == i:
            return True
    return False

# def ile_razy(zdanie,n):
#     suma = 0
#     for i in zdanie:
#         if czy_nalezy(i,n):
#             suma += 1
#     return suma

def slownik(zdanie):
    d = {}
    for i in zdanie:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    return d

print(slownik(zdanie))
