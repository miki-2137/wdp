n = int(input('podaj liczbe: '))  # wzglednie pierwsze-jedyny wspolny dzielnik to 1

def najw_wsp_dzielnik(a, b): 
    if (a == b): return a 
    elif (a > b):  
        return najw_wsp_dzielnik(a - b, b) 
    return najw_wsp_dzielnik(a, b - a) 
  
def wzglednie(a, b): 
    if (najw_wsp_dzielnik(a, b) == 1): 
        return True
---------------------
def wzglednie(a,b):
    x = 1
    for i in range(1,a+1):
        if a%i == 0 and b%i == 0:
            x = i
    return x == 1

def wszystkie(n):
    wz = []
    for i in range(1,n):
        if wzglednie(i,n):
            wz.append(i)
    return wz

print(wszystkie(n))
