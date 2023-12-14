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

    def est_accepte(self, code):
        """
        ->param code : code à compiler

        ->return : list_token, 
                    numéro de ligne de fin de lecture ( permet de retourner la ligne ou il 
        y a une erreur si il y en a une)
                    True ou false suivant la réussite ou non de la lecture complète du code
        """
        token_courant = ''
        ind_cara_lu   = 0
        ligne         = 1
        in_string     = False
        in_const      = False
        self.token_par_ligne.append(0)

        # on va lire caractère par caractère le code
        while ind_cara_lu<len(code):

            cara = code[ind_cara_lu]

            # cas ou on est dans une chaine de caractère
            if in_string and cara != '"':
                token_courant += cara
                ind_cara_lu += 1
                continue

            # cas de fin de constante
            if in_const and not cara.isdigit() and cara != '.':

                #cas de fin de constante
                if token_courant.count('.') > 1:
                    message_erreur = self.gene_message_erreur(token_courant, cara, ligne, "Nombre à virgule invalide")
                    self.etat_comp  = False
                    print(message_erreur)
                    return self.liste_token, ligne, False, message_erreur
                
                # on ajout la constante à la table des constantes
                # on peut alors avoir plusieurs constante identique dans la table des constantes
                self.table_const.append(token_courant)
                self.liste_token.append((7, self.table_const.index(token_courant) + 1))
                self.token_par_ligne[-1]+=1
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
                else:
                    if token_courant not in ('',' ', '\t', '\n'):
                        code_current_token = self.codage_token(token_courant)
                        self.liste_token.append(code_current_token)
                        self.token_par_ligne[-1]+=1
                    # nouvelle ligne donc 0 pour recommencer à compté le nombre de token sur la prochaine ligne
                    self.token_par_ligne.append(0)
                    token_courant = ''
                    ind_cara_lu += 1
                    ligne += 1
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
                    if token_courant not in ('',' ', '\t', '\n'):
                        code_current_token = self.codage_token(token_courant)
                        self.liste_token.append(code_current_token)
                        self.token_par_ligne[-1]+=1
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
                if token_courant not in ('',' ', '\t', '\n'):
                    code_current_token = self.codage_token(token_courant)
                    self.liste_token.append(code_current_token)
                    self.token_par_ligne[-1]+=1

                token_courant = cara
                ind_cara_lu += 1
                in_const = True
                continue


            # cas de détection de caractères spéciaux
            if cara in (';',',',':','(',')','.',"'",'"','+','-','*','/','=','>','<') :
                # cas de début et de fin d 'une chaine de caractère    
                if cara == '"':
                    if in_string:
                        self.table_chaine_cara.append(token_courant)
                        self.liste_token.append((47, self.table_chaine_cara.index(token_courant) + 1))
                        self.token_par_ligne[-1]+=1
                        token_courant = ''
                        in_string = False
                        ind_cara_lu += 1
                        continue
                    else:
                        token_courant = ''
                        in_string = True
                        ind_cara_lu += 1
                        continue
                    
                if cara == '-':

                    if token_courant not in ('',' ', '\t', '\n'):
                        code_current_token = self.codage_token(token_courant)
                        self.liste_token.append(code_current_token)
                        self.token_par_ligne[-1]+=1
                    token_courant = cara
                    ind_cara_lu += 1
                    continue

                # cas de détection de ':='
                if cara == '=' and token_courant == ':'  and not in_string:
                    token_courant += cara
                    ind_cara_lu += 1
                    self.liste_token.append(5)
                    self.token_par_ligne[-1]+=1
                    token_courant = ''
                    continue

                # dans les autres cas le cara n'étant pas dans une chaine de caractère c est donc un séparateur et on place alors 
                # le token courant dans la liste des token
                if token_courant not in ('',' ', '\t', '\n'):
                    code_current_token = self.codage_token(token_courant)
                    if code_current_token != -1 and code_current_token != None and not in_string:
                        self.liste_token.append(code_current_token)
                        self.token_par_ligne[-1]+=1
                        token_courant = ''

                # si on a ':' on ne place pas dans la liste des token car cela oeut être un ':=' e vraie    
                if cara == ':':
                    token_courant += cara
                    ind_cara_lu += 1
                    continue
                
                self.liste_token.append(self.codage_token(cara))
                self.token_par_ligne[-1]+=1
                token_courant = ''
                ind_cara_lu += 1
                continue
            
            if cara in self.alphabet:
                
                token_courant += cara
                ind_cara_lu += 1
                continue

            else:
                # si le caractère n'est traité par aucuns des cas au dessus c'est qu'il n'est pas reconnu
                message_erreur = self.gene_message_erreur(token_courant, cara, ligne, "Caractère non reconnu")
                self.etat_comp  = False
                print(message_erreur)
                return self.liste_token, ligne, False, message_erreur

        if token_courant not in ('',' ', '\t', '\n'):
            self.liste_token.append(self.codage_token(token_courant))
            self.token_par_ligne[-1]+=1
        self.etat_comp = True
        return self.liste_token, ligne, True