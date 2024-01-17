from grammaire import Grammaire, Regle
from automate import *

def parse_syntax(automate, grammaire):

    liste_token = automate.liste_token

    print(liste_token)
    
    positionStream = 0
    stack = [grammaire.axiomeRegle.get_membre_gauche()]
    
    print(grammaire.terminaux)

    while stack:
        current_symbol = stack.pop()


        if isinstance(current_symbol, tuple):
            continue

        if current_symbol in grammaire.token_terminaux:
            if current_symbol == liste_token[positionStream]:
                print(current_symbol)
                positionStream += 1
            else:
                print(f"Erreur: Prévu '{current_symbol}', recu '{liste_token[positionStream]}'")
                return False

        elif current_symbol in grammaire.non_terminaux:
            print(current_symbol)
            listeRegleAjout = grammaire.regleByNonTerminal[current_symbol]
            for regle in listeRegleAjout:
                if regle.get_membre_droit()[0] == liste_token[positionStream]:
                    RegleAjout = regle
            stack.extend(regle.RegleInt[::-1])
            # rule_key = liste_token[positionStream]
            # if rule_key in grammaire.premiersDico[current_symbol]:
            #     production_rule = regleAjout[rule_key][0]
            #     production_right = production_rule.get_membre_droit()
            #     stack.extend(production_right[::-1])
            #     print(stack)
            # else:
            #     print(f"ERREUR: Règle non trouvée pour {current_symbol}, token: {liste_token[positionStream]}")


        elif current_symbol == '$':
            print("Fin atteinte")
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

    if parse_syntax(automate, grammaire):
        print("Analyse syntaxique réussie")
    else:
        print("L'analyse syntaxique à échoué")

if __name__ == "__main__":
    main()
