class Automate:
    def __init__(self, etats = {}, alphabet = {}, transitions = {}, etat_initial = None, etats_finaux = {}):
        self.etats = etats
        self.alphabet = alphabet
        self.transitions = transitions
        self.etat_initial = etat_initial
        self.etats_finaux = etats_finaux

    def codage_token(self, token):
        pass

    def est_accepte(self, code):
        """
        ->param code : code à compiler

        ->return : list_token, 
                    numéro de ligne de fin de lecture ( permet de retourner la ligne ou il 
        y a une erreur si il y en a une)
                    True ou false suivant la réussite ou non de la lecture complète du code
        """

        etat_courant = self.etat_initial
        token_courant = ''
        ind_cara_lu = 0
        ligne = 1
        list_token = []
        while ind_cara_lu<len(code):
            if code[ind_cara_lu] not in self.alphabet:
                # si le caractère n'est pas reconnue, alors on retourne une erreur
                return list_token, ligne, False
            
            else:
                token_courant += code[ind_cara_lu]

                # resultat c'est tout les mots qui commencent par token_courant qui peuvent être reconnue par l'automate
                # ce sont les mots sur les transitions possible à partir de l'état courant
                resultat = [cle for cle in self.transitions.keys() if cle.startswith(token_courant)]

                if resultat == []:
                    # si le token n'est pas reconnue, alors on retourne une erreur
                    return list_token, ligne, False
                
                elif len(resultat) == 1:
                    if resultat[0] == token_courant:
                        # si le token est reconnue, alors on continue la lecture en passant à l'état suivant
                        etat_courant = self.transitions[etat_courant][code[ind_cara_lu]]
                        ind_cara_lu += 1
                    else:
                        ind_cara_lu +=1





