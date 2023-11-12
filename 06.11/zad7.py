import random
lista1 = []
lista2 = []
def generuj1(n,min,max):
    for i in range(0,n):
        lista1.append(random.randint(min,max))

def generuj2(n,min,max):
    for i in range(0,n):
        lista2.append(random.randint(min,max))

def czy_zawiera(lista1,lista2):
    for i in lista2:
        zawiera = False
        for j in lista1:
            if i == j:
                zawiera = True
        if not zawiera:
            return False
    return True


a = int(input('podaj dlugosc listy 1: '))
b = int(input('podaj element minimalny listy 1: '))
c = int(input('podaj element maksymalny listy 1: '))
d = int(input('podaj dlugosc listy 2: '))
e = int(input('podaj element minimalny listy 2: '))
f = int(input('podaj element maksymalny listy 2: '))

def main():
    generuj1(a,b,c)
    generuj2(d,e,f)
    print(lista1,lista2)
    print(czy_zawiera(lista1, lista2))

main()