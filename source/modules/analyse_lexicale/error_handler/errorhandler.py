class ErrorHandler:

    def __init__():
        pass
    
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
            message_erreur = f"Erreur à la ligne  {ligne}  : { type_erreur } : {cara} \n {code} \n{(len(code) - 1)*' '}'^'"
            return message_erreur