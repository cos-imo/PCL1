from grammaire import Grammaire, Regle
from automate import *
from graphviz import *

def parse_syntax(automate, grammaire, display_graph = False):

    liste_token = automate.liste_token

    if display_graph:
        dot = Digraph(comment='Arbre')
    
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

    reglesArbre = ['FICHIER']
    tailleRegle = [[14,0]]

    indice = 0

    while stack:
        current_symbol = stack.pop()
        print(stack)
        print(f"#########{current_symbol = }, {positionStream = } ############")

        print(f"{current_symbol = }")
        print(f"{positionStream = }")
        print(f"{liste_token[positionStream] = }\n\n")

        if isinstance(current_symbol, tuple):
            if current_symbol == (6,2) and stack[-1] == 43 and stack[-2] == (6,3):
                stack.pop()
                stack.pop()
                current_symbol = 49
            else:
                positionStream += 1

        if isinstance(current_symbol, int):
            if current_symbol == liste_token[positionStream]:
                positionStream += 1
                if display_graph:
                    dot.node(str(current_symbol), str(current_symbol))
                    dot.edge(reglesArbre[-1],str(current_symbol))
                try:
                    tailleRegle[-1][1]+=1
                    if tailleRegle[-1][1] == tailleRegle[-1][0]:
                        tailleRegle.pop()
                        regles.pop()
                except:
                    pass
                continue
            else:
                print(f"Erreur: Prévu '{current_symbol}', recu '{liste_token[positionStream]}'")
                return False

        elif current_symbol == 'eof':
            print("Fin atteinte")

            if display_graph:
                dot.view()
                print(reglesArbre)
 
            print("Parsing réussi!")

            print(regles)
            return True

            
        elif isinstance(current_symbol, str):
            if current_symbol == "DECLETOILE":

                if regle.membre_droit:
                    tailleRegle.append([len(regle.membre_droit), 0])
                
                if liste_token[positionStream] == 26:
                    stack.append("DECL")
                    if display_graph:
                        if tailleRegle:
                            if tailleRegle[-1]:
                                reglesArbre.append(f"DECL{indice}")
                                dot.node(f"DECL{indice}", f"DECL{indice}")
                                indice+=1
                                tailleRegle[-1] -= 1
                            else:
                                reglesArbre.append(f"DECL{indice}")
                                tailleRegle.append()
                                dot.node(f"DECL{indice}", f"DECL{indice}")
                                indice+=1
                        else:
                            dot.node(f"DECL{indice}", f"DECL{indice}")
                            indice += 1
                            reglesArbre.append(f"DECL{indice}")
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
                                if display_graph:
                                    if tailleRegle:
                                        if tailleRegle[-1]:
                                            reglesArbre.append(f"{regle.membre_gauche}{indice}")
                                            dot.node(f"{regle.membre_gauche}{indice}", f"{regle.membre_gauche}{indice}")
                                            indice += 1
                                            #dot.edges(reglesArbre[-1], reglesArbre[-2])
                                            dot.edge(regle.membre_gauche, str(reglesArbre[-2]))
                                        else:
                                            tailleRegle.append(len(regle.membre_droit))
                                            reglesArbre.append(regle.membre_gauche)
                                            dot.node(f"{regle.membre_gauche}{indice}", f"{regle.membre_gauche}{indice}")
                                            indice += 1
                                            dot.edge(reglesArbre[-1], reglesArbre[-2])
                                            dot.edge(regle.membre_gauche, reglesArbre[-2])
                                    else:
                                        reglesArbre.append(regle.membre_gauche)
                                        tailleRegle.append(len(regle.membre_droit))
                                        dot.node(f"{regle.membre_gauche}{indice}", f"{regle.membre_gauche}{indice}")
                                        indice += 1
                                stack.extend(RegleAjout.RegleInt[::-1])
                    else:
                        if regle.membre_droit:
                            if regle.RegleInt[0] == liste_token[positionStream]:
                                RegleAjout = regle
                                regles.append(regle.raw_regle)
                                stack.extend(RegleAjout.RegleInt[::-1])
                                if display_graph:
                                    reglesArbre.append(regle.membre_gauche)
                                    tailleRegle.append(len(regle.membre_droit))
                                    dot.node(f"{regle.membre_gauche}{indice}", f"{regle.membre_gauche}{indice}")
                                    indice += 1
                            elif regle.membre_gauche == "IDENT":
                                pass
                        else:
                            if liste_token[positionStream + 1] == 10:
                                #positionStream += 1
                                pass
            else:
                # Gérer l'identifiant
                if isinstance(liste_token[positionStream], tuple):
                    if display_graph:
                        dot.node(automate.table_idf[liste_token[positionStream][1]], automate.table_idf[liste_token[positionStream][1]])
                        dot.edge(reglesArbre[-1], automate.table_idf[liste_token[positionStream][1]])
                else:
                    dot.node("id")
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


# def main():
    
#     fichier = """with Ada.Text_IO;

#                     procedure Proced is
#                     a : integer := 1; 
#                     b : integer := 2;
#                     c : integer := 3;

#                     procedure eq is
#                                 i : integer := 1;
#                             begin
#                                 d := a ; 
#                             end eq;

#                     begin

#                     a := 1; 
#                     b := 1; 

#                     eq;


#                     end Proced;"""


#     automate = Automate()
#     automate.est_accepte(fichier)
#     grammaire = Grammaire.Grammaire()
#     print(automate.table_idf)
#     if parse_syntax(automate, grammaire):
#         print("Analyse syntaxique réussie")
#     else:
#         print("L'analyse syntaxique à échoué")
#         print(automate.liste_token)

# if __name__ == "__main__":
#     main()
