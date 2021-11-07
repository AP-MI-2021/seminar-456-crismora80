from Domain.prajitura import toString, getNume, getDescriere, getPret, getCalorii, getAn
from Logic.CRUD import adaugaPrajitura, stergePrajitura, modificaPrajitura, getById
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
    print("u. Undo")
    print("r. Redo")
    print("a. Afisare prajituri")
    print("x. Iesire")


def uiAdaugaPrajitura(lista, undoOperations, redoOperations):
    try:
        id = input("Dati id-ul: ")
        nume = input("Dati numele: ")
        descriere = input("Dati descrierea: ")
        pret = float(input('Dati pretul: '))
        calorii = int(input("Dati nr. de calorii: "))
        an = int(input("Dati anul introducerii in meniu: "))

        rezultat = adaugaPrajitura(id, nume, descriere, pret, calorii, an, lista)
        undoOperations.append([
            lambda: stergePrajitura(id, rezultat),
            lambda: adaugaPrajitura(id, nume, descriere, pret, calorii, an, lista)
        ])
        redoOperations.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiStergePrajitura(lista, undoOperations, redoOperations):
    try:
        id = input("Dati id-ul prajiturii de sters: ")

        rezultat = stergePrajitura(id, lista)
        prajituraDeSters = getById(id, lista)
        undoOperations.append([
            lambda: adaugaPrajitura(
                id,
                getNume(prajituraDeSters),
                getDescriere(prajituraDeSters),
                getPret(prajituraDeSters),
                getCalorii(prajituraDeSters),
                getAn(prajituraDeSters),
                rezultat),
            lambda: stergePrajitura(id, lista)
        ])
        redoOperations.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiModificaPrajitura(lista, undoOperations, redoOperations):
    try:
        id = input("Dati id-ul prajiturii de modificat: ")
        nume = input("Dati noul nume: ")
        descriere = input("Dati noua descriere: ")
        pret = float(input('Dati noul pret: '))
        calorii = int(input("Dati noul nr. de calorii: "))
        an = int(input("Dati noul an al introducerii in meniu: "))

        rezultat = modificaPrajitura(id, nume, descriere, pret, calorii, an, lista)
        prajituraVeche = getById(id, lista)
        undoOperations.append([
            lambda: modificaPrajitura(
                id,
                getNume(prajituraVeche),
                getDescriere(prajituraVeche),
                getPret(prajituraVeche),
                getCalorii(prajituraVeche),
                getAn(prajituraVeche),
                rezultat),
            lambda: modificaPrajitura(id, nume, descriere, pret, calorii, an, lista)
        ])
        redoOperations.clear()
        return rezultat
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
        print("Anul {} are prajitura cu nr. max. de calorii {}".format(an, toString(rezultat[an])))


def uiOrdonareDupaPretCalorii(lista):
    showAll(ordonareDupaPretCalorii(lista))


def uiSumaPreturiPerAn(lista):
    rezultat = sumaPreturiPerAn(lista)
    for an in rezultat:
        print("Anul {} are suma preturilor {}".format(an, rezultat[an]))

def runMenu(lista):
    undoOperations = []
    redoOperations = []
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")
        
        if optiune == "1":
            lista = uiAdaugaPrajitura(lista, undoOperations, redoOperations)
        elif optiune == "2":
            lista = uiStergePrajitura(lista, undoOperations, redoOperations)
        elif optiune == "3":
            lista = uiModificaPrajitura(lista, undoOperations, redoOperations)
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
        elif optiune == "u":
            if len(undoOperations) > 0:
                operations = undoOperations.pop()
                redoOperations.append(operations)
                lista = operations[0]()
            else:
                print("Nu se poate face undo!")
        elif optiune == "r":
            if len(redoOperations) > 0:
                operations = redoOperations.pop()
                undoOperations.append(operations)
                lista = operations[1]()
            else:
                print("Nu se poate face redo!")
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")

'''
l = []
u = []
r = []

add
l = [1]
u = [[sterge(1), adauga(1)]]
r = []

add
l = [1,2]
u = [[sterge(1), adauga(1)],[sterge(2), adauga(2)]]
r = []

undo
l = [1]
u = [[sterge(1), adauga(1)]]
r = [[sterge(2), adauga(2)]]

undo
l = []
u = []
r = [[sterge(2), adauga(2)], [sterge(1), adauga(1)]]

redo
l = [1]
u = [[sterge(1), adauga(1)]]
r = [[sterge(2), adauga(2)]]

redo
l = [1,2]
u = [[sterge(1), adauga(1)], [sterge(2), adauga(2)]]
r = []
'''