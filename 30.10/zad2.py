def sgn(x):
    if x < 0:
        return -1
    elif x > 0:
        return 1
    else:
        return 0
def main():
    x = float(input('podaj liczbe: '))
    print('znak liczby to', sgn(x))
main()
