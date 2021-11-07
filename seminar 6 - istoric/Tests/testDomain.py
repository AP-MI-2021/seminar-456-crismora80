from Domain.prajitura import creeazaPrajitura, getId, getNume, getDescriere, getPret, getCalorii, getAn


def testPrajitura():
    prajitura = creeazaPrajitura("1", "tiramisu", "italiana", 10, 200, 1995)

    assert getId(prajitura) == "1"
    assert getNume(prajitura) == "tiramisu"
    assert getDescriere(prajitura) == "italiana"
    assert getPret(prajitura) == 10
    assert getCalorii(prajitura) == 200
    assert getAn(prajitura) == 1995
