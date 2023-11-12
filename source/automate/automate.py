import string as string

class Automate:
    def __init__(self):

        self.table_idf = []
        self.table_const = []
        self.liste_token = []
        self.alphabet = string.ascii_lowercase + string.ascii_uppercase + "_"

        #le codage des unités lexicales se trouve dans le fichier codage_dse_lexique.txt
        self.mots = ['+','-','*','/',':=', None, None,
            "access", "and", "begin", "else", "elsif", "end",
            "false", "for", "function", "if", "in", "is",
            "loop", "new", "not", "null", "or", "out",
            "procedure", "record", "rem", "return", "reverse", "then",
            "true", "type", "use", "while", "with", ':', '(', ')', ',', ';', '=', '.', "'",'>','<'
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
        in_const = False

        # on va lire caractère par caractère le code
        while ind_cara_lu<len(code):

            cara = code[ind_cara_lu]

            # cas de fin de string
            if in_string and cara != '"':
                token_courant += cara
                ind_cara_lu += 1
                continue

            # cas de fin de constante
            if in_const and not cara.isdigit() and cara != '.':
                #cas de fin de constante
                if token_courant not in self.table_const:
                    self.table_const.append(token_courant)
                list_token.append((7, self.table_const.index(token_courant) + 1))
                token_courant = ''
                in_const = False

            # cas de commentaire
            if cara == '-' and token_courant == '-' and not in_string:
                #on ignire alors tout les caractères jusqu'à la fin de la ligne
                while cara != '\n':
                    ind_cara_lu += 1
                    cara = code[ind_cara_lu]
                ligne += 1
                token_courant = ''
                continue

                
            if cara == '\n':
                # si on est dans une chaine de caractrère on ajoute le \n au token courant 
                # sinon on rajout juste le token courant à la liste des token et on ignore le caractère '\n'
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

                # on garde les espaces dans les chaines de caractères
                if in_string:
                    token_courant += cara
                    ind_cara_lu += 1
                    continue


                # cas d'esapce hors chaine de caractère, on ignore alors juste ce caractère

                # cas de plmusieurs espaces à la suite
                if token_courant == '':
                    ind_cara_lu += 1
                    continue
                else:
                    code_current_token = self.codage_token(token_courant)
                    if code_current_token != -1 and code_current_token != None:
                        list_token.append(code_current_token)
                    ind_cara_lu += 1
                    token_courant = ''
                    continue

            # on garde le points dans les constantes pour pouvoir prendre les floatants
            if in_const :
                if cara == '.' or cara.isdigit():
                    token_courant += cara
                    ind_cara_lu += 1
                    continue
            

            # cas de début de constante
            if cara.isdigit():
                token_courant += cara
                ind_cara_lu += 1
                in_const = True
                continue


            # cas de détection de caractères spéciaux
            if cara in (';',',',':','(',')','.',"'",'"','+','-','*','/','=','>','<') :

                # cas de détection de ':='
                if cara == '=' and token_courant == ':'  and not in_string:
                    token_courant += cara
                    ind_cara_lu += 1
                    list_token.append(5)
                    token_courant = ''
                    continue

                # dans les autres cas le cara n'étant pas dans une chaine de caractère c est donc un séparateur et on place alors 
                # le token courant dans la liste des token
                code_current_token = self.codage_token(token_courant)
                if code_current_token != -1 and code_current_token != None and not in_string:
                    list_token.append(code_current_token)
                    token_courant = ''

                # si on a ':' on ne place pas dans la liste des token car cela oeut être un ':=' e vraie    
                if cara == ':':
                    token_courant += cara
                    ind_cara_lu += 1
                    continue
                    
                # cas de début d 'une chaine de caractère    
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
        
        for token in self.liste_token:

            if isinstance(token, tuple):
                if token[0] == 6:
                    code += self.table_idf[token[1] - 1]
                elif token[0] == 7:
                    code += self.table_const[token[1] - 1]
                else:
                    code += self.alphabet[token[0] - 1]
            elif isinstance(token, int):
                code += self.mots[token - 1]
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
