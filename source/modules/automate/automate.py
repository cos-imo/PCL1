import string as string

class Automate:
    def __init__(self):

        self.table_idf         = []   # liste avec tout les identifiants détectés dans le code
        self.table_const       = []   # liste avec tout les constantes détectés dans le code
        self.table_chaine_cara = []   # liste avec tout les chaines de caractères détectés dans le code
        self.liste_token       = []   # liste avec tout les token du code
        self.error_message     = []
        self.alphabet          = string.ascii_letters + string.digits + '_'
        self.table_error_token = []   # liste avec tout les token qui ne sont pas reconnue


        self.etat_comp = None #None avant lecture, True si réussite, False si échec
        self.token_par_ligne = [] # liste des nombre de token par ligne (ça va permettre de retrouver la ligne d'erreur lors de l'analyse syntaxique)

        #le codage des unités lexicales se trouve dans le fichier codage_dse_lexique.txt
        self.mots = ['+','-','*','/',':=', None, None,
            "access", "and", "begin", "else", "elsif", "end",
            "false", "for", "function", "if", "in", "is",
            "loop", "new", "not", "null", "or", "out",
            "procedure", "record", "rem", "return", "reverse", "then",
            "true", "type", "use", "while", "with", ':', '(', ')', ',', ';', '=', '.', "'",'>','<'
        ]

    def print_error(self):
        """
        Affiche les erreurs de compilation
        """
        for error in self.error_message:
            print(error)


    def codage_token(self, token):
        """
        ->param token : token à coder

        ->return : code du token ou -1 si le token n'est pas reconnu

        les codes des tokens sont disponible dans le fichier documents/codage_dse_lexique.txt
        
        """

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
    
    def gene_message_erreur(self, token_courant, cara, ligne, type_erreur):
        """
        ->param token_courant : token courant
        ->param cara : caractère non reconnu
        ->param ligne : numéro de ligne du caractère non reconnu
        ->param type_erreur : type d'erreur rencontré

        ->return : message d'erreur
        """
        code = ""
        #on va boucler à l'envers sur la liste des token pour retrouver le dernier ':' et donc print toute la ligne



        # on va dabors récupére les derniers token analyser (on récupère la dernière ligne de code)
        code = token_courant 
        ind = 0
        if self.liste_token[-1] == 41:
            code = ':' + code
            ind += 1

        # on recupère alors tout les token de la ligne actuelle (ou précédante si on est en début de ligne)
        while self.liste_token[-ind] != 41 and ind < len(self.liste_token) -2:

            # on réécrit le code en passant de token=>code
            if isinstance(self.liste_token[-ind], tuple):
                if self.liste_token[-ind][0] == 6:
                    code = self.table_idf[self.liste_token[-ind][1] - 1]    + code

                elif self.liste_token[-ind][0] == 7:
                    code = self.table_const[self.liste_token[-ind][1] - 1]  + code

                elif self.table_chaine_cara[-ind][0] == 47:
                    code = '"' + self.table_chaine_cara[self.liste_token[-ind][1] - 1] + '"' + code
                else:
                    code = self.alphabet[self.liste_token[-ind][0] - 1]     + code

            elif isinstance(self.liste_token[-ind], int):
                code = self.mots[self.liste_token[-ind] - 1] + code
            
            code =' ' + code
            ind += 1
        code +=  '_'

        # création du message d'erreur
        message_erreur = f"\033[91mErreur à la ligne  {ligne}\033[0m  : { type_erreur } : {cara} \n {code} \n{(len(code) - 1)*' '}'^'"
        return message_erreur



    def est_accepte(self, code):
        """
        ->param code : code à compiler, chemin d'accès au fichier

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
                print(cara)
                # si le caractère n'est traité par aucuns des cas au dessus c'est qu'il n'est pas reconnu
                message_erreur = self.gene_message_erreur(token_courant, cara, ligne, "Caractère non reconnu")
                self.etat_comp  = False
                self.error_message.append(message_erreur)
                self.table_error_token.append(token_courant + cara)
                self.liste_token.append((48, len(self.table_error_token)))
                ind_cara_lu += 1
                token_courant = ''

        if token_courant not in ('',' ', '\t', '\n'):
            self.liste_token.append(self.codage_token(token_courant))
            self.token_par_ligne[-1]+=1
        if self.etat_comp == None:
            self.etat_comp = True

    def reconstruction(self, adresse_txt):
        """
        ->return : code reconstruit à partir de la liste de token
        """
        code = ''
        if self.etat_comp == False:
            return "Erreur de compilation, reconstruction impossible"
        compteur_token = 0
        num_ligne = 0
        for token in self.liste_token:
            if compteur_token == self.token_par_ligne[num_ligne]:
                code += '\n'
                num_ligne += 1
                compteur_token = 0
                while self.token_par_ligne[num_ligne] == 0:
                    num_ligne += 1
                    code += '\n'

            if isinstance(token, tuple):
                if token[0] == 6:
                    code += self.table_idf[token[1] - 1]
                if token[0] == 7:
                    code += self.table_const[token[1] - 1]
                if token[0] == 47:
                    code += '"'  + self.table_chaine_cara[token[1] - 1] + '"'

            elif isinstance(token, int):
                code += self.mots[token - 1]
            code +=' '
            compteur_token += 1
        
        def ecrire_code_reconstruit(self, adresse_txt):
            """
            Écrit le code reconstruit dans le fichier texte à l'adresse spécifiée.
            """
            with open(adresse_txt, 'w') as f:
                f.write(code)
        ecrire_code_reconstruit(self, adresse_txt)



def main(fichier):
    automate = Automate()

    with open(fichier, 'r') as file:
        code = file.read()

    automate.est_accepte(code)
    print('\n')
    print(f'{automate.table_const = }')
    print('\n')
    print(f'{automate.table_idf = }')
    print('\n')
    print(f'{automate.table_chaine_cara = }')
    print('\n')
    print(f'code tokenizé : {automate.liste_token}') 
    
    automate.print_error()
        
    """        ###
        if not code_compi[2]:
            print(code_compi[3])
        print(automate.token_par_ligne)
        ###
    """

    reconstruit = automate.reconstruction("fichier_reconstruit.txt")


if __name__ == "__main__":
    main("exemple_ada_.txt")