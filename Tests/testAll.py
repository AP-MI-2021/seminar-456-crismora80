from Tests.testCRUD import testAdaugaPrajitura, testStergePrajitura, testModificaPrajitura
from Tests.testDomain import testPrajitura
from Tests.testFunctionalitati import testReducereCalorii


def runAllTests():
    testPrajitura()
    testAdaugaPrajitura()
    testStergePrajitura()
    testModificaPrajitura()
    testReducereCalorii()