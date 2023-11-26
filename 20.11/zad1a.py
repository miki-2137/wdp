n = int(input('podaj liczbe: '))  # wzglednie pierwsze-jedyny wspolny dzielnik to 1

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