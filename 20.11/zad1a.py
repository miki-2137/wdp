n = int(input('podaj liczbe: '))

def dzielniki(liczba):
    dzielnik = []
    for i in range(1,int(liczba/2+1)):
        if liczba % i == 0:
            dzielnik.append(i)
    return dzielnik

def wz()

def main():
    print(dzielniki(n))
main()