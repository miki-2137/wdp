import random
lista = []
def generuj(n, min, max):
    for i in range(0, n):
        lista.append(random.randint(min, max))

def ile_ujemnych(list):
    u = 0
    for i in list:
        if i < 0:
            u += 1
    return u

def main():
    a = int(input('Podaj długość listy: '))
    b = int(input('Podaj element minimalny: '))
    c = int(input('Podaj element maksymalny: '))
    generuj(a,b,c)
    print(ile_ujemnych(lista))

main()
