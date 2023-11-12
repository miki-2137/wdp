import random
lista = []
def generuj(n,min,max):
    for i in range(0,n):
        lista.append(random.randint(min,max))

def minmax(list):
    min = list[0]
    max = list[0]
    for i in list:
        if i < min:
            min = i
        elif i > max:
            max = i
    return (min,max)

a = int(input('podaj dlugosc listy: '))
b = int(input('podaj element minimalny: '))
c = int(input('podaj element maksymalny: '))

def main():
    generuj(a,b,c)
    print(lista)
    print(minmax(lista))

main()