n = int(input('podaj liczbe: '))

def fibonacci(n):
    fb = []
    for i in range(0,n+1):
        if i == 0:
            fb.append(0)
        elif i == 1:
            fb.append(1)
        else:
            fb.append(fb[i-1]+fb[i-2])
    return fb

def mn(n):
    m = []
    for i in fibonacci(n):
        if i < n:
            m.append(i)
    return m

print(mn(n))