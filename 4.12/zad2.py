a = int(input('podaj ilosc liczb: '))

def liczby(a):
    liczby = []
    for i in range(1,a+1):
        i = input('podaj  liczbe: ')
        if isinstance(i, int):
            liczby.append(i)
        else:
            print('podaj liczbe calkowita!!!')
    return liczby

def slownik(liczby):
    d = {}
    for i in liczby:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    return d

print(slownik(liczby(a)))
