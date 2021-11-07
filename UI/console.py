from Domain.prajitura import toString
from Logic.CRUD import adaugaPrajitura, stergePrajitura, modificaPrajitura
from Logic.functionalitate import reducereCalorii


def printMenu():
    print("1. Adaugare prajitura")
    print("2. Stergere prajitura")
    print("3. Modificare prajitura")
    print("4. Reducere nr. calorii")
    print("a. Afisare prajituri")
    print("x. Iesire")


def uiAdaugaPrajitura(lista):
    id = input("Dati id-ul: ")
    nume = input("Dati numele: ")
    descriere = input("Dati descrierea: ")
    pret = float(input('Dati pretul: '))
    calorii = int(input("Dati nr. de calorii: "))
    an = int(input("Dati anul introducerii in meniu: "))
    return adaugaPrajitura(id, nume, descriere, pret, calorii, an, lista)


def uiStergePrajitura(lista):
    id = input("Dati id-ul prajiturii de sters: ")
    return stergePrajitura(id, lista)


def uiModificaPrajitura(lista):
    id = input("Dati id-ul prajiturii de modificat: ")
    nume = input("Dati noul nume: ")
    descriere = input("Dati noua descriere: ")
    pret = float(input('Dati noul pret: '))
    calorii = int(input("Dati noul nr. de calorii: "))
    an = int(input("Dati noul an al introducerii in meniu: "))
    return modificaPrajitura(id, nume, descriere, pret, calorii, an, lista)


def showAll(lista):
    for prajitura in lista:
        print(toString(prajitura))


def uiReducereCalorii(lista):
    substringNume = input("Dati substringul numelui pt. care prajiturilor li se va reduce nr. de calorii")
    caloriiReduse = int(input("Dati valoarea cu care vreti sa reduceti caloriile: "))
    return reducereCalorii(substringNume, caloriiReduse, lista)


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
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")