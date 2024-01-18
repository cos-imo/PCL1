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

    regles = []

    for terminal in grammaire.terminaux:
        if terminal:
            automate.est_accepte(terminal)
            token_terminaux.append(automate.liste_token)

    while stack:
        current_symbol = stack.pop()
        print(stack)
        print(f"#########{current_symbol = }, {positionStream = } ############")

        print(f"{current_symbol = }")
        print(f"{positionStream = }")
        print(f"{liste_token[positionStream] = }\n\n")

        if isinstance(current_symbol, tuple):
            print(f"{stack[-1] = }")
            print(f"{stack[-2] = }")
            if current_symbol == (6,2) and stack[-1] == 43 and stack[-2] == (6,3):
                print("Passage au 49")
                stack.pop()
                stack.pop()
                current_symbol = 49
            else:
                positionStream += 1

        if isinstance(current_symbol, int):
            print(f"{liste_token[positionStream] = }")
            if current_symbol == liste_token[positionStream]:
                positionStream += 1
                continue
            else:
                print(f"Erreur: Prévu '{current_symbol}', recu '{liste_token[positionStream]}'")
                return False

        elif current_symbol == 'eof':
            print("Fin atteinte")

 
            print("Parsing réussi!")

            print(regles)
            return True

            
        elif isinstance(current_symbol, str):
            print(f"{liste_token[positionStream + 1] =}")
            if current_symbol == "DECLETOILE":
                if liste_token[positionStream] == 26:
                    stack.append("DECL")
                    continue
                if liste_token[positionStream]==10:
                    continue

            if current_symbol != "id":
                listeRegleAjout = grammaire.regleByNonTerminal[current_symbol]
                for regle in listeRegleAjout:
                    if isinstance(liste_token[positionStream], tuple):
                        if regle.premier:
                            if "id" in regle.premier:
                                RegleAjout = regle
                                regles.append(regle.raw_regle)
                                stack.extend(RegleAjout.RegleInt[::-1])
                    else:
                        if regle.membre_droit:
                            if regle.RegleInt[0] == liste_token[positionStream]:
                                RegleAjout = regle
                                regles.append(regle.raw_regle)
                                stack.extend(RegleAjout.RegleInt[::-1])
                            elif regle.membre_gauche == "IDENT":
                                print(f"{liste_token[positionStream] = }")
                                pass
                        else:
                            if liste_token[positionStream + 1] == 10:
                                #positionStream += 1
                                pass
            else:
                # Gérer l'identifiant
                positionStream += 1
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

                    procedure Proced is
                    a : integer := 1; 
                    b : integer := 2;
                    c : integer := 3;

                    procedure eq is
                                i : integer := 1;
                            begin
                                d := a ; 
                            end eq;

                    begin

                    a := 1; 
                    b := 1; 

                    eq;


                    end Proced;"""


    automate = Automate()
    automate.est_accepte(fichier)
    grammaire = Grammaire.Grammaire()
    print(automate.table_idf)
    if parse_syntax(automate, grammaire):
        print("Analyse syntaxique réussie")
    else:
        print("L'analyse syntaxique à échoué")
        print(automate.liste_token)

if __name__ == "__main__":
    main()
