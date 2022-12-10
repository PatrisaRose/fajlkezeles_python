def beolvas(fajlnev):
    fajlom = open(fajlnev, "r", encoding='utf-8')
    print(fajlom)
    """fajltartalom = fajlom.read()
    print(fajltartalom)"""
    fejlec = fajlom.readline().strip()
    print(fejlec)
    sorok = fajlom.readlines()
    print(sorok)
    fajlom.close()
    fajlfeldolgozas(sorok)

    """Ez a fejléc"""
    """fajlom.readline()
    fajl_tartalom = fajlom.readlines()
    fajlom.close()"""

nevek = []
nemek = []
korok = []

def fajlfeldolgozas(sorok):
    """Itt dolgozom fel a listát"""
    i = 0
    while i < len(sorok):
        print(sorok[i].strip())
        sor = sorok[i].strip().split(',')
        print(sor)
        nevek.append(sor[0])
        nemek.append(sor[1])
        korok.append(sor[2])
        i += 1
    print(nevek)
    print(nemek)
    print(korok)