from grammaire import Grammaire, Regle
from automate import *

def parse_syntax(automate, grammaire):

    liste_token = automate.liste_token

    
    positionStream = 0
    stack = [grammaire.axiomeRegle.get_membre_gauche()]

    token_terminaux = []

    if liste_token[1:4] == [(6, 1), 43, (6, 2)]:
        del liste_token[1:4]
        liste_token.insert(1, 49)

    print(liste_token)
    
    for terminal in grammaire.terminaux:
        if terminal:
            automate.est_accepte(terminal)
            token_terminaux.append(automate.liste_token)

    while stack:
        current_symbol = stack.pop()
        print(stack)


        if isinstance(current_symbol, tuple):
            print(automate.table_idf[current_symbol[1]])
            positionStream += 1
            continue

        if isinstance(current_symbol, int):
            if current_symbol == liste_token[positionStream]:
                print(current_symbol)
                positionStream += 1
            else:
                print(f"Erreur: Prévu '{current_symbol}', recu '{liste_token[positionStream]}'")
                return False

        elif current_symbol == '$':
            print("Fin atteinte")
            if positionStream == len(liste_token):
                print("Parsing réussi!")
                return True
            else:
                print("Erreur: token après $")
                return False
            
        elif isinstance(current_symbol, str):
            listeRegleAjout = grammaire.regleByNonTerminal[current_symbol]
            for regle in listeRegleAjout:
                if regle.RegleInt[0] == liste_token[positionStream]:
                    RegleAjout = regle
            stack.extend(RegleAjout.RegleInt[::-1])
            # rule_key = liste_token[positionStream]
            # if rule_key in grammaire.premiersDico[current_symbol]:
            #     production_rule = regleAjout[rule_key][0]
            #     production_right = production_rule.get_membre_droit()
            #     stack.extend(production_right[::-1])
            #     print(stack)
            # else:
            #     print(f"ERREUR: Règle non trouvée pour {current_symbol}, token: {liste_token[positionStream]}")

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


    automate = Automate()
    automate.est_accepte(fichier)
    grammaire = Grammaire.Grammaire()

    if parse_syntax(automate, grammaire):
        print("Analyse syntaxique réussie")
    else:
        print("L'analyse syntaxique à échoué")

if __name__ == "__main__":
    main()
