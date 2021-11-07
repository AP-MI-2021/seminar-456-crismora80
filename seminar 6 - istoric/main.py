from Logic.CRUD import adaugaPrajitura
from Tests.testAll import runAllTests
from UI.console import runMenu

def main():
    runAllTests()
    lista = []
    lista = adaugaPrajitura("1", "tiramisu", "italiana", 10, 200, 1995, lista)
    lista = adaugaPrajitura("2", "ecler", "vanilie", 12, 300, 2015, lista)
    runMenu(lista)

main()


'''
    nume = "Morarescu"
    prenume = "Cristina"
    varsta = 26
    s = "Numele meu este {} {} si am {} ani".format(nume, prenume, varsta)
    print(s)
'''

'''
    l = [1,2,3,4,5]
    l2 = [x*x for x in l if x%2 == 1]
    print(l2)
    
    l2 = []
    for x in l:
        if ...
            l2.append(x)
    print(l2)
'''