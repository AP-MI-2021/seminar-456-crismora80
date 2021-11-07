from Domain.prajitura import getNume, creeazaPrajitura, getId, getDescriere, getPret, getCalorii, getAn


def reducereCalorii(substringNume, caloriiReduse, lista):
    """
    reduce numarul de calorii ale prajiturilor ale caror nume contin un string dat
    :param substringNume: stringul dupa care se cauta numele
    :param caloriiReduse:  numarul de calorii ce se reduc
    :param lista: lista de prajituri
    :return: lista in care prajiturile ale caror nume contin stringul dat s-au modificat
    """
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