from grammaire import Grammaire, Regle
from automate import *

def parse_syntax(liste_token, grammaire):
    positionStream = 0
    stack = [grammaire.axiomeRegle.get_membre_gauche()]

    while stack:
        current_symbol = stack.pop()

        if isinstance(current_symbol, tuple):
            continue

        if current_symbol in grammaire.terminaux:
            if current_symbol == liste_token[positionStream]:
                positionStream += 1
            else:
                print(f"Erreur: Prévu '{current_symbol}', recu '{liste_token[positionStream]}'")
                return False

        elif current_symbol in grammaire.non_terminaux:
            rule_key = liste_token[positionStream]
            if rule_key in grammaire.regle_by_premier[current_symbol]:
                production_rule = grammaire.regle_by_premier[current_symbol][rule_key][0]
                production_right = production_rule.get_membre_droit()
                stack.extend(production_right[::-1])

        elif current_symbol == '$':
            if positionStream == len(liste_token):
                print("Parsing réussi!")
                return True
            else:
                print("Erreur: token après $")
                return False

        else:
            print(f"Erreur: Token inconnu '{current_symbol}'")

    return False


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

    if parse_syntax(liste_token, grammaire):
        print("Analyse syntaxique réussie")
    else:
        print("L'analyse syntaxique à échoué")

if __name__ == "__main__":
    main()
