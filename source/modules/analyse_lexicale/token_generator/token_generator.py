from token_analyser import * 
import string

class tokeniser_t:

    def __init__(self):
        self.liste_token=[]
        self.Analyser=token_analyser_t()
        self.alphabet = string.ascii_lowercase + string.ascii_uppercase + "_"
        self.analyser = token_analyser_t() 

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