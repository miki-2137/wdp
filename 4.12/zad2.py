def liczby():
    liczby = []
    while True:
        i = input('podaj liczbe: ')
        if not i:
            break
        try:
            i = int(i)
        except ValueError:
            print('to nie jest liczba calkowita!!!')
        else:
            liczby.append(i)
    return liczby


def slownik(liczby):
    d = {}
    for i in liczby:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    return d

print(slownik(liczby()))
