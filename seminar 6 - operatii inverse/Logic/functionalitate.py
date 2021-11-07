from Domain.prajitura import getNume, creeazaPrajitura, getId, getDescriere, getPret, getCalorii, getAn


def reducereCalorii(substringNume, caloriiReduse, lista):
    """
    reduce numarul de calorii ale prajiturilor ale caror nume contin un string dat
    :param substringNume: stringul dupa care se cauta numele
    :param caloriiReduse:  numarul de calorii ce se reduc
    :param lista: lista de prajituri
    :return: lista in care prajiturile ale caror nume contin stringul dat s-au modificat
    """
    if caloriiReduse < 0:
        raise ValueError("Nr. de calorii reduse trebuie sa fie pozitiv!")
    listaNoua = []
    for prajitura in lista:
        if substringNume in getNume(prajitura):
            prajituraNoua = creeazaPrajitura(
                getId(prajitura),
                getNume(prajitura),
                getDescriere(prajitura),
                getPret(prajitura),
                getCalorii(prajitura) - caloriiReduse,
                getAn(prajitura)
            )
            listaNoua.append(prajituraNoua)
        else:
            listaNoua.append(prajitura)
    return listaNoua

def prajituriMaiRecenteDecatAn(an, lista):
    '''

    :param an:
    :param lista:
    :return:
    '''
    listaNoua = []
    for prajitura in lista:
        if getAn(prajitura) > an:
            listaNoua.append(prajitura)
    return listaNoua

def maxCaloriiPerAn(lista):
    '''

    :param lista:
    :return:
    '''
    rezultat = {}
    for prajitura in lista:
        an = getAn(prajitura)
        calorii = getCalorii(prajitura)
        if an in rezultat:
            if calorii > getCalorii(rezultat[an]):
                rezultat[an] = prajitura
        else:
            rezultat[an] = prajitura
    return rezultat

def raportPretCalorii(prajitura):
    return getPret(prajitura) / getCalorii(prajitura)

def ordonareDupaPretCalorii(lista):
    '''

    :param lista:
    :return:
    '''
    #return sorted(lista, key=lambda prajitura: getPret(prajitura)/getCalorii(prajitura))
    return sorted(lista, key=raportPretCalorii)

def sumaPreturiPerAn(lista):
    '''

    :param lista:
    :return:
    '''
    rezultat = {}
    for prajitura in lista:
        an = getAn(prajitura)
        pret = getPret(prajitura)
        if an in rezultat:
            rezultat[an] = rezultat[an] + pret
        else:
            rezultat[an] = pret
    return rezultat
