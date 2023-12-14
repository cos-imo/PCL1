class data_exporter:
    def __init__(self):
        pass

    def create_dump_file(self, tokens, dump_mode):
        with open("dump_file", "w+") as file:
            for token in tokens:
                file.write(str(token))

    def ecrire_code_reconstruit(self, adresse_txt):
        """
        Écrit le code reconstruit dans le fichier texte à l'adresse spécifiée.
        """
        with open(adresse_txt, 'w') as f:
            f.write(code)

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