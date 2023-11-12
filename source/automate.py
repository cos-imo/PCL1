class Automate:
    def __init__(self):

        self.table_idf = []
        self.table_const = []
        self.liste_token = []
        self.alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_'

    def codage_token(self, token):
            if token == "\n":
                return -1
            
            
            if token == '':
                return None
            
            if token.isdigit():
                if token not in self.table_const:
                    self.table_const.append(token)
                return (7, self.table_const.index(token) + 1)

            #le codage des unités lexicales se trouve dans le fichier codage_dse_lexique.txt
            mots = ['+','-','*','/',':=', None, None,
            "access", "and", "begin", "else", "elsif", "end",
            "false", "for", "function", "if", "in", "is",
            "loop", "new", "not", "null", "or", "out",
            "procedure", "record", "rem", "return", "reverse", "then",
            "true", "type", "use", "while", "with", ':', '(', ')', ',', ';', '=', '.', "'",'>','<'
        ]
            if token in mots:
                return mots.index(token) + 1
            
            if token[0].isalpha():
                if token not in self.table_idf:
                    self.table_idf.append(token)
                return (6, self.table_idf.index(token) + 1)

            # enfin si un caractère n'est pas reconnue : on renvoie un token d'erreur de valeur -1
            return (-1, token)


    def est_accepte(self, code):
        """
        ->param code : code à compiler

        ->return : list_token, 
                    numéro de ligne de fin de lecture ( permet de retourner la ligne ou il 
        y a une erreur si il y en a une)
                    True ou false suivant la réussite ou non de la lecture complète du code
        """
        token_courant = ''
        ind_cara_lu = 0
        ligne = 1
        list_token = []
        in_string = False
        while ind_cara_lu<len(code):
            cara = code[ind_cara_lu]

            if in_string and cara != '"':
                token_courant += cara
                ind_cara_lu += 1
                continue

            if cara == '-' and token_courant == '-' and not in_string:
                while cara != '\n':
                    ind_cara_lu += 1
                    cara = code[ind_cara_lu]
                ligne += 1
                token_courant = ''
                continue
            if cara == '-' and not in_string:
                code_current_token = self.codage_token(token_courant)
                if code_current_token != -1 and code_current_token != None:
                    list_token.append(code_current_token)
                token_courant = cara
                ind_cara_lu += 1
                continue
                


            if cara == '\n':
                if in_string:
                    token_courant += cara
                    ind_cara_lu += 1
                    continue
                ligne += 1
                ind_cara_lu += 1
                if token_courant != '':
                    code_current_token = self.codage_token(token_courant)
                    if code_current_token != -1:
                        list_token.append(code_current_token)
                    else:
                        return list_token, ligne, False
                    token_courant = ''
                    continue


            if cara == ' ' or cara == '\t':
                if in_string:
                    token_courant += cara
                    ind_cara_lu += 1
                    continue
                if token_courant == '':
                    ind_cara_lu += 1
                    continue
                code_current_token = self.codage_token(token_courant)
                if code_current_token != -1 and code_current_token != None:
                    list_token.append(code_current_token)
                ind_cara_lu += 1
                token_courant = ''
                continue

            if cara in (';',',',':','(',')','.',"'",'"','+','-','*','/','=','>','<') :

                if cara == '=' and token_courant == ':'  and not in_string:
                    token_courant += cara
                    ind_cara_lu += 1
                    list_token.append(5)
                    token_courant = ''
                    continue

                code_current_token = self.codage_token(token_courant)
                if code_current_token != -1 and code_current_token != None and not in_string:
                    list_token.append(code_current_token)
                    token_courant = ''

                if cara == ':':

                    token_courant += cara
                    ind_cara_lu += 1
                    continue
                    
                if cara == '"':
                    if in_string:
                        list_token.append(self.codage_token(token_courant))
                        token_courant = ''
                        in_string = False
                        ind_cara_lu += 1

                        continue
                    else:
                        token_courant = ''
                        in_string = True
                        ind_cara_lu += 1
                        continue

                
                list_token.append(self.codage_token(cara))
                token_courant = ''
                ind_cara_lu += 1
                continue
            
            if cara in self.alphabet:
                token_courant += cara
                ind_cara_lu += 1
                continue

            else:
                ind_cara_lu += 1



        list_token.append(self.codage_token(token_courant))
        self.liste_token = list_token
        return list_token[:-1], ligne, True

    def reconstruction(self, adresse_txt):
        """
        ->return : code reconstruit à partir de la liste de token
        """
        code = ''
        mots = ['+','-','*','/',':=', None, None,
            "access", "and", "begin", "else", "elsif", "end",
            "false", "for", "function", "if", "in", "is",
            "loop", "new", "not", "null", "or", "out",
            "procedure", "record", "rem", "return", "reverse", "then",
            "true", "type", "use", "while", "with", ':', '(', ')', ',', ';', '=', '.', "'",'>','<'
        ]
        for token in self.liste_token:

            if isinstance(token, tuple):
                if token[0] == 6:
                    code += self.table_idf[token[1] - 1]
                elif token[0] == 7:
                    code += self.table_const[token[1] - 1]
                else:
                    code += self.alphabet[token[0] - 1]
            elif isinstance(token, int):
                code += mots[token - 1]
            if code[-1] == ';':
                code += "\n"
            else:
                code +=' '

            
            
        
        def ecrire_code_reconstruit(self, adresse_txt):
            """
            Écrit le code reconstruit dans le fichier texte à l'adresse spécifiée.
            """
            with open(adresse_txt, 'w') as f:
                f.write(code)
        ecrire_code_reconstruit(self, adresse_txt)



automate = Automate()

with open('exemple_ada_.txt', 'r') as f:
    code = f.read()
    print(automate.est_accepte(code))


reconstruit = automate.reconstruction("fichier_reconstruit.txt")