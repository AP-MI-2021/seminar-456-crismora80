def creeazaPrajitura(id, nume, descriere, pret, calorii, an):
    '''
    creaza un dictiionar ce reprezinta o prajitura
    :param id: string
    :param nume: string
    :param descriere: string
    :param pret: float
    :param calorii: int
    :param an: int
    :return: un dictionar ce contine o prajitura
    '''
    return {
        "id": id,
        "nume": nume,
        "descriere": descriere,
        "pret": pret,
        "calorii": calorii,
        "an": an
    }

def getId(prajitura):
    '''
    da id-ul unei prajituri
    :param prajitura: dictionar ce contine o prajitura
    :return: id-ul prajiturii
    '''
    return prajitura["id"]

def getNume(prajitura):
    return prajitura["nume"]

def getDescriere(prajitura):
    return prajitura["descriere"]

def getPret(prajitura):
    return prajitura["pret"]

def getCalorii(prajitura):
    return prajitura["calorii"]

def getAn(prajitura):
    return prajitura["an"]

def toString(prajitura):
    return "Id: {}, Nume: {}, Descriere: {}, Pret: {}, Calorii: {}, An: {}".format(
        getId(prajitura),
        getNume(prajitura),
        getDescriere(prajitura),
        getPret(prajitura),
        getCalorii(prajitura),
        getAn(prajitura)
    )
