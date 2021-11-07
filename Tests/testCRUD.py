from Domain.prajitura import getId, getNume, getDescriere, getCalorii, getPret, getAn
from Logic.CRUD import adaugaPrajitura, getById, stergePrajitura, modificaPrajitura


def testAdaugaPrajitura():
    lista = []
    lista = adaugaPrajitura("1", "tiramisu", "italiana", 10, 200, 1995, lista)

    assert len(lista) == 1
    assert getId(getById("1", lista)) == "1"
    assert getNume(getById("1", lista)) == "tiramisu"
    assert getDescriere(getById("1", lista)) == "italiana"
    assert getPret(getById("1", lista)) == 10
    assert getCalorii(getById("1", lista)) == 200
    assert getAn(getById("1", lista)) == 1995

def testStergePrajitura():
    lista = []
    lista = adaugaPrajitura("1", "tiramisu", "italiana", 10, 200, 1995, lista)
    lista = adaugaPrajitura("2", "ecler", "italiana", 10, 200, 1995, lista)

    lista = stergePrajitura("1", lista)

    assert len(lista) == 1
    assert getById("1", lista) is None
    assert getById("2", lista) is not None

    lista = stergePrajitura("3", lista)

    assert len(lista) == 1
    assert getById("2", lista) is not None

def testModificaPrajitura():
    lista = []
    lista = adaugaPrajitura("1", "tiramisu", "italiana", 10, 200, 1995, lista)
    lista = adaugaPrajitura("2", "ecler", "vanilie", 10, 200, 1995, lista)

    lista = modificaPrajitura("1", "sarailie", "dulce", 5, 500, 2010, lista)

    prajituraUpdatata = getById("1", lista)
    assert getId(prajituraUpdatata) == "1"
    assert getNume(prajituraUpdatata) == "sarailie"
    assert getDescriere(prajituraUpdatata) == "dulce"
    assert getPret(prajituraUpdatata) == 5
    assert getCalorii(prajituraUpdatata) == 500
    assert getAn(prajituraUpdatata) == 2010

    prajituraNeupdatata = getById("2", lista)
    assert getId(prajituraNeupdatata) == "2"
    assert getNume(prajituraNeupdatata) == "ecler"
    assert getDescriere(prajituraNeupdatata) == "vanilie"
    assert getPret(prajituraNeupdatata) == 10
    assert getCalorii(prajituraNeupdatata) == 200
    assert getAn(prajituraNeupdatata) == 1995

    lista = []
    lista = adaugaPrajitura("1", "tiramisu", "italiana", 10, 200, 1995, lista)

    lista = modificaPrajitura("3", "sarailie", "dulce", 5, 500, 2010, lista)

    prajituraNeupdatata = getById("1", lista)
    assert getId(prajituraNeupdatata) == "1"
    assert getNume(prajituraNeupdatata) == "tiramisu"
    assert getDescriere(prajituraNeupdatata) == "italiana"
    assert getPret(prajituraNeupdatata) == 10
    assert getCalorii(prajituraNeupdatata) == 200
    assert getAn(prajituraNeupdatata) == 1995
