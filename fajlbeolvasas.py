import random


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
    adatok(sorok)

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
        sor = sorok[i].strip().split(', ')
        print(sor)
        nevek.append(sor[0])
        nemek.append(sor[1])
        korok.append(int(sor[2]))
        i += 1
    print(nevek)
    print(nemek)
    print(korok)

def adatok(sorok):
    i = 0
    c = 0
    while i < len(sorok):
        sor = sorok[i].strip().split(', ')
        c += len(sor)
        i += 1
    print(c)

def atlag():
    atlag = sum(korok)/len(korok)
    print(atlag)

def no():
    i = 0
    c = 0
    while i < len(nemek):
        if nemek[i] == 'nő':
            c += 1
        i += 1
    print(f"Ennyi nő van összesen: {c}")


def legfiatalabb_no():
    i = 0
    legfiatalabb = 248
    while i < len(nemek):
        if nemek[i] == 'nő':
            if korok[i] < legfiatalabb:
                legfiatalabb = korok[i]
        i += 1
    print(f"Ennyi éves a legfiatalabb nő: {legfiatalabb}")

def adatsor():
    nev = input('Kérlek adj meg egy nevet: ')
    nem = ''
    while nem != 'férfi' and nem != 'nő':
        nem = input('Kérlek add meg a nemet: ')
    kor = int(random.random()*71)+10
    adatok = open('teszt.txt', 'a', encoding='utf-8')
    adatok.write(f"\n{nev}, {nem}, {kor}")
    adatok.close()
