from modules.grammaire.Regle import Regle

class testRegle:

    def __init__(self, testList = None):
        # for function in testList:
        #     if function in globals() and callable(globals()[function]):
        #         function = globals()[function]
        #         res = function()
        #         print(f"Test {function}: {res}")
        #     else:
        #         print(f"Fonction {function} non trouvée.")
        # pass
        if testList:
            for test in testList:
                regletest = Regle(testList.index(test), test)
                print(regletest)
        else:
            regletest = Regle(0, "S -> a b c")
            print(regletest)




if __name__=="__main__":
    test = testRegle()