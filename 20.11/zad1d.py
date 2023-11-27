n = int(input('podaj liczbe: '))

def fibonacci(n):
    fb = []
    for i in range(0,n+1):
        if i < 2:
            fb.append(i)
        else:
            fb.append(fb[i-1]+fb[i-2])
    return fb

def mn(n):
    m = 0
    for i in fibonacci(n):
        if i < n:
            m = i
    return m

print(mn(n))