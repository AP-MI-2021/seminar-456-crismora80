from Domain.prajitura import creeazaPrajitura, getId


def adaugaPrajitura(id, nume, descriere, pret, calorii, an, lista):
    '''
    adauga o prajitura intr-o lista
    :param id: string
    :param nume: string
    :param descriere: string
    :param pret: float
    :param calorii: int
    :param an: int
    :param lista: lista de prajituri
    :return: o lista continand atat elementele vechi, cat si noua prajitura
    '''
    if getById(id, lista) is not None:
        raise ValueError("Id-ul exista deja!")
    prajitura = creeazaPrajitura(id, nume, descriere, pret, calorii, an)
    return lista + [prajitura]

def getById(id, lista):
    '''
    gaseste o prajitura cu id-ul dat intr-o lista
    :param id: string
    :param lista: lista de prajituri
    :return: prajitura cu id-ul dat din lista sau None, daca aceasta nu exista
    '''
    for prajitura in lista:
        if getId(prajitura) == id:
            return prajitura
    return None

def stergePrajitura(id, lista):
    """
    sterge o prajitura cu id-ul dat din lista
    :param id: id-ul prajiturii care se va sterge
    :param lista: lista de prajituri
    :return: o lista de prajituri fara elementul cu id-ul dat
    """
    if getById(id, lista) is None:
        raise ValueError("Nu exista o prajitura cu id-ul dat!")
    return [prajitura for prajitura in lista if getId(prajitura) != id]

def modificaPrajitura(id, nume, descriere, pret, calorii, an, lista):
    """
    modifica a prajitura cu id-ul dat
    :param id: id-ul prajiturii
    :param nume: numele prajiturii
    :param descriere: descrierea prajiturii
    :param pret: pretul prajiturii
    :param calorii: nr. de calorii al prajiturii
    :param an: anul introducerii in meniu al prajiturii
    :param lista: O lista de prajituri.
    :return: lista modificata.
    """
    if getById(id, lista) is None:
        raise ValueError("Nu exista o prajitura cu id-ul dat!")
    listaNoua = []
    for prajitura in lista:
        if getId(prajitura) == id:
            prajituraNoua = creeazaPrajitura(id, nume, descriere, pret, calorii, an)
            listaNoua.append(prajituraNoua)
        else:
            listaNoua.append(prajitura)
    return listaNoua