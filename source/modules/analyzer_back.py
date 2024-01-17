from grammaire import *
from automate import *

def main():
    fichier = """with Ada.Text_IO;

    procedure exemple is
    n : integer ; 
    begin
    loop
        Ada.Text_IO.Put("Saisir un nombre : ") ;
        Ada.Text_IO.Get(n) ; 
        if n mod 2 := 0
            then Ada.Text_IO.Put("Ce nombre est pair ! Bien joué !") ;
            else Ada.Text_IO.Put("Ce nombre est impair ! Veuillez recommencer. ") ; 
        end if ; 
    end loop ; 
    end exemple ;"""

    grammaire = Grammaire.Grammaire()

    automate = Automate()
    automate.est_accepte(fichier)

    liste_token = automate.liste_token

    print(liste_token)

    positionStream = 0

    currentRule = grammaire.axiomeRegle

    Rules = []
    
    while positionStream < len(liste_token):
        positionRule = 0
        while currentRule.RegleInt[positionRule] == liste_token[positionStream]:
            positionRule += 1
            positionStream += 1
            print(positionStream)
            print(liste_token[positionStream])
        Rules.append(currentRule)
        if isinstance(liste_token[positionStream], int):
            currentRule = grammaire.regle_by_premier[liste_token[positionStream]]
    
    #print(Rules)

if __name__=="__main__":
    main()