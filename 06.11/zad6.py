import random
lista = []
def generuj(n,min,max):
    for i in range(0,n):
        lista.append(random.randint(min,max))

def czy_nalezy(lista,element):
    for i in lista:
        if element == i:
            return True
    return False


a = int(input('podaj dlugosc listy: '))
b = int(input('podaj element minimalny: '))
c = int(input('podaj element maksymalny: '))
element = int(input('podaj element: '))

def main():
    generuj(a,b,c)
    print(lista)
    print(czy_nalezy(lista, element))

main()