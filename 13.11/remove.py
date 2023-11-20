napis = "abrakadabra"
usuwany = "ab"

def remove(napis, usuwany):
    for i in range(len(napis)):
        if napis[i] == usuwany[0]:
            d = i + len(usuwany)
            us = napis[i:d]
            if usuwany == us:
                return napis[:i] + napis[d:]
    return napis

def remove_all(napis, usuwany):
    wynik = napis
    for i in range(len(napis)):
        if napis[i] == usuwany[0]:
            d = i + len(usuwany)
            us = napis[i:d]
            if usuwany == us:
                wynik = napis[:i] + napis[d:]
                for j in range(len(wynik)):
                    if remove(wynik, usuwany) != wynik:
                        wynik = remove(wynik,usuwany)
    return wynik


def main():
    print(remove(napis,usuwany))
    print(remove_all(napis,usuwany))

main()