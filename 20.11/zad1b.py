n = int(input('podaj liczbe: '))

def dzielniki(n):
    dz = []
    for i in range(1,(int(n/2)+1)):
        if n%i == 0:
            dz.append(i)
    return dz

def czy_doskonala(n):
    suma = 0
    for i in dzielniki(n):
        suma += i
    if suma == n:
        return True
    return False

def doskonale_mniejsze(n):
    dosk = []
    for i in range(1,n):
        if czy_doskonala(i) == True:
            dosk.append(i)
    return dosk

print(doskonale_mniejsze(n))