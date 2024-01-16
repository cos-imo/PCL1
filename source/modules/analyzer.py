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

    liste_token = automate.liste_token

    current_regle = grammaire.axiome

    # for token in liste_token:
    #     if token in 

    #print(grammaire.premiers_non_terminaux)

if __name__=="__main__":
    main()