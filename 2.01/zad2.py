#jest podzielny przez 4, ale nie jest podzielny przez 100 lub jest podzielny przez 400

rok = int(input('podaj rok: '))

def czy_przestepny(rok):
    if rok %4 == 0:
        if rok %100 == 0 and rok %400 != 0:
            return False
        else:
            return True
    else:
        return False

print(czy_przestepny(rok))
