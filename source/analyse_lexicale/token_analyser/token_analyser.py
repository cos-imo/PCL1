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

    def codage_token(self, token):
        if token == "\n":
            return -1
        
        if token == '':
            return None
        
        if token.isdigit():
            if token not in self.table_const:
                self.table_const.append(token)
            return (7, self.table_const.index(token) + 1)

        if token in self.mots:
            return self.mots.index(token) + 1
        
        if token[0].isalpha():
            if token not in self.table_idf:
                self.table_idf.append(token)
            return (6, self.table_idf.index(token) + 1)

        # enfin si un caractère n'est pas reconnu : on renvoie un token d'erreur de valeur -1
        return (-1, token)

