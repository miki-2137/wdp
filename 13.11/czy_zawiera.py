def czy_nalezy(lista,element):
    for i in lista:
        if i == element:
            return True
    return False

def czy_zawiera(lista1, lista2):
    for i in lista2:
        if not czy_nalezy(lista1,i):
            return False
    return True

lista1 = [1,2,3,4,5]
lista2 = [2,3]

print(czy_zawiera(lista1,lista2))