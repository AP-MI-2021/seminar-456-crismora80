from Tests.testCRUD import testAdaugaPrajitura, testStergePrajitura, testModificaPrajitura
from Tests.testDomain import testPrajitura
from Tests.testFunctionalitati import testReducereCalorii, testPrajituriMaiRecenteDecatAn, testMaxCaloriiPerAn, \
    testOrdonareDupaPretCalorii, testSumaPreturiPerAn


def runAllTests():
    testPrajitura()
    testAdaugaPrajitura()
    testStergePrajitura()
    testModificaPrajitura()

    testReducereCalorii()
    testPrajituriMaiRecenteDecatAn()
    testMaxCaloriiPerAn()
    testOrdonareDupaPretCalorii()
    testSumaPreturiPerAn()