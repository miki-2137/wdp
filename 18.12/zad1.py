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
        return 'zle haslo!!!'
    else:
        return 'dobre haslo'

print(haslo(slownik(pwd)))
