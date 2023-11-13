napis = 'abrakadabra'
usuwany = 'ab'

def remove(napis,usuwany):
    napis = napis.replace(usuwany,'',1)
    return napis

def remove_all(napis,usuwany):
    for i in napis:
        napis = napis.replace(usuwany,'',1)
    return napis

def main():
    print(remove(napis,usuwany))
    print(remove_all(napis,usuwany))

main()
