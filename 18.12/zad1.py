pwd = 'Password'

def slownik(string):
    d = {}
    for i in string:
        if not i.isalpha():
            d[i] = 1
        elif i.isupper():
            d[i] = 1
    return d

print(slownik(pwd))

def haslo(d):
    if len(d)<2:
        return 'chujowe haslo lmao l+ratio'
    else:
        return 'gituwa haslo szefie 8)))'

print(haslo(slownik(pwd)))
