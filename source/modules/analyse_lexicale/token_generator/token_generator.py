from token_analyser import * 
import string

class tokeniser_t:

    def __init__(self):
        self.liste_token=[]
        self.Analyser=token_analyser_t()
        self.alphabet = string.ascii_lowercase + string.ascii_uppercase + "_"
        self.analyser = token_analyser_t() 

    def est_accepte(self, code):
        """
        ->param code : code à compiler

        ->return : list_token, 
                    numéro de ligne de fin de lecture ( permet de retourner la ligne ou il 
        y a une erreur si il y en a une)
                    True ou false suivant la réussite ou non de la lecture complète du code
        """
        token_courant = ''
        peak_index = 0
        ligne = 1
        list_token = []
        in_string = False
        in_const = False

        # on va lire caractère par caractère le code
        while peak_index<len(code):

            peak = code[peak_index]

            # cas de fin de string
            if in_string and peak != '"':
                token_courant += peak
                peak_index += 1
                continue

            # cas de fin de constante
            if in_const and not peak.isdigit() and peak != '.':
                #cas de fin de constante
                if token_courant not in self.table_const:
                    self.table_const.append(token_courant)
                list_token.append((7, self.table_const.index(token_courant) + 1))
                token_courant = ''
                in_const = False

            # cas de commentaire
            if peak == '-' and token_courant == '-' and not in_string:
                #on ignire alors tout les caractères jusqu'à la fin de la ligne
                while peak != '\n':
                    peak_index += 1
                    peak = code[peak_index]
                ligne += 1
                token_courant = ''
                continue

                
            if peak == '\n':
                # si on est dans une chaine de caractrère on ajoute le \n au token courant 
                # sinon on rajout juste le token courant à la liste des token et on ignore le caractère '\n'
                if in_string:
                    token_courant += peak
                    peak_index += 1
                    continue
                ligne += 1
                peak_index += 1

                if token_courant != '':
                    code_current_token = self.analyser.codage_token(token_courant)
                    if code_current_token != -1:
                        list_token.append(code_current_token)
                    else:
                        return list_token, ligne, False
                    token_courant = ''
                    continue

            if peak == ' ' or peak == '\t':

                # on garde les espaces dans les chaines de caractères
                if in_string:
                    token_courant += peak
                    peak_index += 1
                    continue


                # cas d'esapce hors chaine de caractère, on ignore alors juste ce caractère

                # cas de plmusieurs espaces à la suite
                if token_courant == '':
                    peak_index += 1
                    continue
                else:
                    code_current_token = self.analyser.codage_token(token_courant)
                    if code_current_token != -1 and code_current_token != None:
                        list_token.append(code_current_token)
                    peak_index += 1
                    token_courant = ''
                    continue

            # on garde le point dans les constantes pour pouvoir prendre les floatants
            if in_const :
                if peak == '.' or peak.isdigit():
                    token_courant += peak
                    peak_index += 1
                    continue

            # cas de début de constante
            if peak.isdigit():
                token_courant += peak
                peak_index += 1
                in_const = True
                continue


            # cas de détection de caractères spéciaux
            if peak in (';',',',':','(',')','.',"'",'"','+','-','*','/','=','>','<') :

                # cas de détection de ':='
                if peak == '=' and token_courant == ':'  and not in_string:
                    token_courant += peak
                    peak_index += 1
                    list_token.append(5)
                    token_courant = ''
                    continue

                # dans les autres cas le peak n'étant pas dans une chaine de caractère c est donc un séparateur et on place alors 
                # le token courant dans la liste des token
                code_current_token = self.analyser.codage_token(token_courant)
                if code_current_token != -1 and code_current_token != None and not in_string:
                    list_token.append(code_current_token)
                    token_courant = ''

                # si on a ':' on ne place pas dans la liste des token car cela oeut être un ':=' e vraie    
                if peak == ':':
                    token_courant += peak
                    peak_index += 1
                    continue
                    
                # cas de début d 'une chaine de caractère    
                if peak == '"':
                    if in_string:
                        list_token.append(self.analyser.codage_token(token_courant))
                        token_courant = ''
                        in_string = False
                        peak_index += 1
                        continue
                    else:
                        token_courant = ''
                        in_string = True
                        peak_index += 1
                        continue
                
                list_token.append(self.analyser.codage_token(peak))
                token_courant = ''
                peak_index += 1
                continue
            
            if peak in self.alphabet:
                token_courant += peak
                peak_index += 1
                continue

            else:
                peak_index += 1

        list_token.append(self.analyser.codage_token(token_courant))
        self.liste_token = list_token
        return list_token[:-1], ligne, True
