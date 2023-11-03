table_idf=[]

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
        if token not in table_idf:
            table_idf.append(token)
        return (6, table_idf.index(token) + 1)

    # enfin si un caractère n'est pas reconnue : on renvoie un token d'erreur de valeur -1
    return (-1, token)

