class token_analyser_t():

    def __init__(self):
        self.table_idf = []
        #le codage des unités lexicales se trouve dans le fichier codage_dse_lexique.txt
        self.mots = ['+','-','*','/',':=', None, None,
        "access", "and", "begin", "else", "elsif", "end",
        "false", "for", "function", "if", "in", "is",
        "loop", "new", "not", "null", "or", "out",
        "procedure", "record", "rem", "return", "reverse", "then",
        "true", "type", "use", "while", "with", ':', '(', ')', ',', ';', '=', '.', "'"
        ]

    def analyse_token_compr(self, token):

        if token == "" or token == "\n":
            return (-1, token)
        
        if token.isdigit():
            return (7, token)

        

        if token in self.mots:
            return self.mots.index(token) + 1
        
        if token[0].isalpha():
            if token not in self.table_idf:
                self.table_idf.append(token)
            return (6, self.table_idf.index(token) + 1)

        # enfin si un caractère n'est pas reconnue : on renvoie un token d'erreur de valeur -1
        return (-1, token)

