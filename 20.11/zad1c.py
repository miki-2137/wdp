n = int(input('podaj liczbe: '))

def dzielniki(n):
    dz = []
    for i in range(1,n+1):
        if n%i == 0:
            dz.append(i)
    return dz
    
def czy_pierwsza(n):
    if dzielniki(n) == [1,n]:
        return True
    return False
    
def mn_od(n):
    mn = []
    for i in dzielniki(n):
        if czy_pierwsza(i) == True:
            mn.append(i)
    return mn
    
print(dzielniki(n))
print(czy_pierwsza(n))
print(mn_od(n))
