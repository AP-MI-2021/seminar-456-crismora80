from Domain.prajitura import toString
from Logic.CRUD import adaugaPrajitura, stergePrajitura, modificaPrajitura
from Logic.functionalitate import reducereCalorii, prajituriMaiRecenteDecatAn, maxCaloriiPerAn, ordonareDupaPretCalorii, \
    sumaPreturiPerAn


def printMenu():
    print("1. Adaugare prajitura")
    print("2. Stergere prajitura")
    print("3. Modificare prajitura")
    print("4. Reducere nr. calorii")
    print("5. Afișarea tuturor prăjiturilor introduse începând cu un an dat")
    print("6. Determinarea prăjiturii cu cel mai mare număr de calorii din fiecare an al introducerii")
    print("7. Ordonarea prăjiturilor crescător după raportul preț / calorii")
    print("8. Afișarea sumelor prețurilor pentru fiecare an al introducerii")
    print("a. Afisare prajituri")
    print("x. Iesire")


def uiAdaugaPrajitura(lista):
    try:
        id = input("Dati id-ul: ")
        nume = input("Dati numele: ")
        descriere = input("Dati descrierea: ")
        pret = float(input('Dati pretul: '))
        calorii = int(input("Dati nr. de calorii: "))
        an = int(input("Dati anul introducerii in meniu: "))
        return adaugaPrajitura(id, nume, descriere, pret, calorii, an, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiStergePrajitura(lista):
    try:
        id = input("Dati id-ul prajiturii de sters: ")
        return stergePrajitura(id, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiModificaPrajitura(lista):
    try:
        id = input("Dati id-ul prajiturii de modificat: ")
        nume = input("Dati noul nume: ")
        descriere = input("Dati noua descriere: ")
        pret = float(input('Dati noul pret: '))
        calorii = int(input("Dati noul nr. de calorii: "))
        an = int(input("Dati noul an al introducerii in meniu: "))
        return modificaPrajitura(id, nume, descriere, pret, calorii, an, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def showAll(lista):
    for prajitura in lista:
        print(toString(prajitura))

def uiReducereCalorii(lista):
    try:
        substringNume = input("Dati substringul numelui pt. care prajiturilor li se va reduce nr. de calorii")
        caloriiReduse = int(input("Dati valoarea cu care vreti sa reduceti caloriile: "))
        return reducereCalorii(substringNume, caloriiReduse, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiPrajituriMaiRecenteDecatAn(lista):
    try:
        an = int(input("Dati anul: "))
        showAll(prajituriMaiRecenteDecatAn(an, lista))
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiMaxCaloriiPerAn(lista):
    rezultat = maxCaloriiPerAn(lista)
    for an in rezultat:
        print("Anul {} are caloriile maxime {}".format(an, rezultat[an]))


def uiOrdonareDupaPretCalorii(lista):
    showAll(ordonareDupaPretCalorii(lista))


def uiSumaPreturiPerAn(lista):
    rezultat = sumaPreturiPerAn(lista)
    for an in rezultat:
        print("Anul {} are suma preturilor {}".format(an, rezultat[an]))

def runMenu(lista):
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")
        
        if optiune == "1":
            lista = uiAdaugaPrajitura(lista)
        elif optiune == "2":
            lista = uiStergePrajitura(lista)
        elif optiune == "3":
            lista = uiModificaPrajitura(lista)
        elif optiune == "4":
            lista = uiReducereCalorii(lista)
        elif optiune == "5":
            uiPrajituriMaiRecenteDecatAn(lista)
        elif optiune == "6":
            uiMaxCaloriiPerAn(lista)
        elif optiune == "7":
            uiOrdonareDupaPretCalorii(lista)
        elif optiune == "8":
            uiSumaPreturiPerAn(lista)
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")