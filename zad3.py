# suma poteg liczby 2 dla wykladnikow 1-63

suma = 0

for i in range(1, 64):
    suma += 2**i
    print('2 ^', i, '=', 2**i)

print('suma kwadratow:', suma)
