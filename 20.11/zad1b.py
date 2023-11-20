def dzielniki(n):
    dzielnik = []
    for i in range(1,int(n/2+1)):
        if n % i == 0:
            dzielnik.append(i)
    return dzielnik

def suma(dzielnik):
    suma = 0
    for i in dzielnik:
        suma += i
    return suma

def czy_doskonala(n):
    dz = dzielniki(n)
    su = suma(dz)
    return su == n

def liczby(n):
    dosk = []
    for i in range(1,n+1):
        if czy_doskonala(i):
            dosk.append(i)
    return dosk

def main():
    n = int(input('podaj liczbe: '))
    print(dzielniki(n))
    print(czy_doskonala(n))
    print(liczby(n))

main()