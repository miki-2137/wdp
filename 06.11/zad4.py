import random
lista = []
def generuj(n,min,max):
    for i in range(0,n):
        lista.append(random.randint(min,max))

def iloczyn(lista):
    u = 1
    for i in lista:
        u *= i
    return u

a = int(input('podaj dlugosc listy: '))
b = int(input('podaj element minimalny: '))
c = int(input('podaj element maksymalny: '))

def main():
    generuj(a,b,c)
    print(lista)
    print(iloczyn(lista))

main()