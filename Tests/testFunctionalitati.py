from Domain.prajitura import getCalorii, getId
from Logic.CRUD import adaugaPrajitura, getById
from Logic.functionalitate import reducereCalorii, prajituriMaiRecenteDecatAn, maxCaloriiPerAn, ordonareDupaPretCalorii, \
    sumaPreturiPerAn


def testReducereCalorii():
    lista = []
    lista = adaugaPrajitura("1", "abc", "desc1", 12, 13, 1, lista)
    lista = adaugaPrajitura("2", "xyz", "desc1", 12, 13, 1, lista)
    lista = adaugaPrajitura("3","bcd","desc2",12,13,1, lista)

    lista = reducereCalorii("bc",10,lista)

    assert getCalorii(getById("1", lista)) == 3
    assert getCalorii(getById("2", lista)) == 13
    assert getCalorii(getById("3", lista)) == 3

def testPrajituriMaiRecenteDecatAn():
    lista = []
    lista = adaugaPrajitura("1", "tiramisu", "italiana", 10, 200, 1995, lista)
    lista = adaugaPrajitura("2", "ecler", "italiana", 10, 200, 2005, lista)

    rezultat = prajituriMaiRecenteDecatAn(2001, lista)

    assert len(rezultat) == 1
    assert getById("2", lista) is not None

    rezultat = prajituriMaiRecenteDecatAn(2010, lista)

    assert len(rezultat) == 0

def testMaxCaloriiPerAn():
    lista = []
    lista = adaugaPrajitura("1", "tiramisu", "italiana", 10, 100, 1995, lista)
    lista = adaugaPrajitura("2", "ecler", "italiana", 10, 300, 2000, lista)
    lista = adaugaPrajitura("3", "amandina", "ciocolata", 10, 200, 1995, lista)

    rezultat = maxCaloriiPerAn(lista)

    assert len(rezultat) == 2
    assert rezultat[1995] == 200
    assert rezultat[2000] == 300

def testOrdonareDupaPretCalorii():
    lista = []
    lista = adaugaPrajitura("1", "tiramisu", "italiana", 150, 100, 1995, lista)
    lista = adaugaPrajitura("2", "ecler", "italiana", 10, 300, 2000, lista)
    lista = adaugaPrajitura("3", "amandina", "ciocolata", 100, 200, 1995, lista)

    rezultat = ordonareDupaPretCalorii(lista)

    assert getId(rezultat[0]) == "2"
    assert getId(rezultat[1]) == "3"
    assert getId(rezultat[2]) == "1"

def testSumaPreturiPerAn():
    lista = []
    lista = adaugaPrajitura("1", "tiramisu", "italiana", 150, 100, 1995, lista)
    lista = adaugaPrajitura("2", "ecler", "italiana", 10, 300, 2000, lista)
    lista = adaugaPrajitura("3", "amandina", "ciocolata", 100, 200, 1995, lista)

    rezultat = sumaPreturiPerAn(lista)

    assert len(rezultat) == 2
    assert rezultat[1995] == 250
    assert rezultat[2000] == 10