#zad2
#a
lista = []
i = 1
while i < 11:
    lista.append(i)
    i += 1
print(lista)
#b
lista = []
i = 0
while i < 11:
    lista.append(2*i)
    i += 1
print(lista)
#c
lista = []
i = 1
while i < 11:
    lista.append(i**2)
    i += 1
print(lista)
#d
lista = []
i = 1
while i < 11:
    lista.append(0)
    i += 1
print(lista)
#e
lista = []
i = 1
while i < 6:
    lista.append(0)
    lista.append(1)
    i += 1
print(lista)
#f
lista = []
i = 0
while i < 5:
    lista.append(i)
    i += 1
    if i > 4:
        lista += lista
print(lista)
