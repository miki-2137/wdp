n = int(input('podaj liczbe: '))

def kwadraty(n):
    kw = []
    for i in range(0,n):
        for j in range(0,n):
            for k in range(0,n):
                if i**2+j**2+k**2 == n:
                    kw.extend((i,j,k))
    return kw

print(kwadraty(n))