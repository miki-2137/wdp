pwd = 'Password '

def slownik(string):
    d = {}
    for i in string:
        if not i.isalpha():
            if not i.isspace():
                d[i] = 1
        elif i.isupper():
            d[i] = 1
    return d

def haslo(d):
    if len(d) < 2:
        return False
    else:
        return True

print(haslo(slownik(pwd)))
