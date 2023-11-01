

file = open("exemple_ada_.txt", "r")

table_idf = []




def tokeniser(file):
    """Fonction qui prend en paramètre un fichier et qui renvoie une liste de tokens"""

    liste_token = []
    for line in file:
        liste_token_ligne = []
        ligne = list(line)

        # on efface les commentaires
        if '-' in ligne and ligne[ligne.index('-') + 1] == '-':
            del ligne[ligne.index('-'):]
        
        #on va créer les tokens 
        token = ""
        in_string = False
        for ind,lettre in enumerate(ligne):
            if (lettre == " " or lettre  == "\n") and not in_string:

                # on est la dans le cas ou on a un token qui est fini et on est pas dans une chaine de caractères
                if token != "":

                    #c est ici qu on va analyser le token et codé les unités lexicales
                    tuple_token = analyse_token_compr(token)
                    liste_token_ligne.append(tuple_token)

                    token = ""
            else :
                if lettre == '"' and not in_string:
                    # c est le début d un chaine de caractère

                    liste_token_ligne.append(token)
                    token = ""
                    in_string = True
                    continue

                elif lettre == '"' and in_string:
                    # c est la fin d une chaine de caractère

                    in_string = False
                    liste_token_ligne.append((11,token))
                    token = ""
                    continue
                
                elif lettre in (';',',',':','(',')','.',"'") and not in_string:
                    #on doit vérifier si on a := ou juste : 

                    if lettre == ':' and ligne[ind+1] == '=':
                        token += lettre
                        continue

                    if token !='':
                        liste_token_ligne.append(analyse_token_compr(token))
                    liste_token_ligne.append(analyse_token_compr(lettre))
                    token = ""
                    continue
                token += lettre
        if liste_token_ligne != []:
            liste_token.append(liste_token_ligne)
        
    return liste_token




def analyse_token_compr(token):


    if token == "" or token == "\n":
        return (-1, token)
    
    if token.isdigit():
        return (7, token)

    #le codage des unités lexicales se trouve dans le fichier codage_dse_lexique.txt
    mots = ['+','-','*','/',':=', None, None,
    "access", "and", "begin", "else", "elsif", "end",
    "false", "for", "function", "if", "in", "is",
    "loop", "new", "not", "null", "or", "out",
    "procedure", "record", "rem", "return", "reverse", "then",
    "true", "type", "use", "while", "with", ':', '(', ')', ',', ';', '=', '.', "'"
]
    if token in mots:
        return mots.index(token) + 1
    
    if token[0].isalpha():
        global table_idf
        if token not in table_idf:
            table_idf.append(token)
        return (6, table_idf.index(token) + 1)

    # enfin si un caractère n'est pas reconnue : on renvoie un token d'erreur de valeur -1
    return (-1, token)



liste = tokeniser(file)

prog_tokeniser = []
for ligne in liste:
    if len(ligne) > 1:
        for token in ligne:
            prog_tokeniser.append(token)
print(prog_tokeniser)

print(table_idf)