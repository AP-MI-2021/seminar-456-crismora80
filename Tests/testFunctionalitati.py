from Domain.prajitura import getCalorii
from Logic.CRUD import adaugaPrajitura, getById
from Logic.functionalitate import reducereCalorii


def testReducereCalorii():
    lista = []
    lista = adaugaPrajitura("1", "abc", "desc1", 12, 13, 1, lista)
    lista = adaugaPrajitura("2", "xyz", "desc1", 12, 13, 1, lista)
    lista = adaugaPrajitura("3","bcd","desc2",12,13,1, lista)

    lista = reducereCalorii("bc",10,lista)

    assert getCalorii(getById("1", lista)) == 3
    assert getCalorii(getById("2", lista)) == 13
    assert getCalorii(getById("3", lista)) == 3