pwd = 'Password@'

def slownik(string):
    d = {}
    if len(string)<8:
        return d
    for i in string:
        if not i.isalpha():
            if not i.isspace():
                d[i] = 1
            else:
                return d
        elif i.isupper():
            d[i] = 1
    return d

def haslo(d):
    if len(d) < 2:
        return False
    else:
        return True

print(haslo(slownik(pwd)))


------------------------------------
pwd = 'Password1'

def haslo(tekst):
    czyCyfra = False
    czyDuza = False
    czyMala = False
    for i in tekst:
        if i.isupper():
            czyDuza = True
        elif i.islower():
            czyMala = True
        elif i.isnumeric():
            czyCyfra = True
    return czyDuza and czyCyfra and czyMala

print(haslo(pwd))
