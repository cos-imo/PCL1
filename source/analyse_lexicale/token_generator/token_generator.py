from token_analyser import * 

class tokeniser_t:

    def __init__(self):
        self.liste_token=[]
        self.Analyser=token_analyser_t()

    @staticmethod
    def tokeniser(self, file):
        """Fonction qui prend en paramètre un fichier et qui renvoie une liste de tokens"""


        for line in file:
            self.liste_token_ligne = []
            ligne = list(line)

            # On efface les commentaires
            if '-' in ligne and ligne[ligne.index('-') + 1] == '-':
                del ligne[ligne.index('-'):]
            
            # On va créer les tokens 
            token = ""
            in_string = False
            for ind,lettre in enumerate(ligne):
                if (lettre == " " or lettre  == "\n") and not in_string:

                    # On est là dans le cas ou on a un token qui est fini et on est pas dans une chaine de caractères
                    if token != "":

                        # C'est ici qu on va analyser le token et coder les unités lexicales
                        tuple_token = self.Analyser.analyse_token_compr(token)
                        self.liste_token_ligne.append(tuple_token)

                        token = ""
                else :
                    if lettre == '"' and not in_string:
                        # C'est le début d un chaîne de caractère

                        self.liste_token_ligne.append(token)
                        token = ""
                        in_string = True
                        continue

                    elif lettre == '"' and in_string:
                        # c est la fin d une chaine de caractère

                        in_string = False
                        self.liste_token_ligne.append((11,token))
                        token = ""
                        continue
                    
                    elif lettre in (';',',',':','(',')','.',"'") and not in_string:
                        # On doit vérifier si on a := ou juste : 

                        if lettre == ':' and ligne[ind+1] == '=':
                            token += lettre
                            continue

                        if token !='':
                            self.liste_token_ligne.append(self.Analyser.analyse_token_compr(token))
                        self.liste_token_ligne.append(self.Analyser.analyse_token_compr(lettre))
                        token = ""
                        continue
                    token += lettre
            if self.liste_token_ligne != []:
                self.liste_token.append(self.liste_token_ligne)
            
        return self.liste_token

    def verbose(self,file):
        liste = tokeniser_t.tokeniser(self, file)

        prog_tokeniser = []
        for ligne in liste:
            if len(ligne) > 1:
                for token in ligne:
                    prog_tokeniser.append(token)
        print(prog_tokeniser)

        print(self.Analyser.table_idf)

