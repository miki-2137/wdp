# suma kwadratow od 1 do 100 wlacznie

suma = 0

for i in range(1, 101):
    print('liczba:', i, '; jej kwadrat:', i**2)
    suma += i**2  # lub suma += math.pow(i,2)

print('suma kwadratow:', suma)
