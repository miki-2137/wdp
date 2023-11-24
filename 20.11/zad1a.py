n = int(input('podaj liczbe: ')) #wzglednie pierwsze-jedyny wspolny dzielnik to 1

def czy_nalezy(lista,element):
    for i in lista:
        if i == element:
            return True
    return False

def dzielniki(n):
    dz = []
    for i in range(1,n):
        if n%i == 0:
            dz.append(i)
    return dz
    
def wzglednie(n):
    wz = []
    for i in range(1,n):
        
    
print(dzielniki(n))
print(wzglednie(n))
