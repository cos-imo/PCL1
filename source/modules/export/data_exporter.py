class data_exporter:
    def __init__(self):
        pass

    def create_dump_file(self, tokens, dump_mode):
        with open("output/dump_file", "w+") as file:
            for token in tokens:
                file.write(str(token))

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