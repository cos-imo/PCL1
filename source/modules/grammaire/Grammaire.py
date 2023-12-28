import sys
import Regle
import RegleManager

class Grammaire:
    def __init__(self):
        self.grammaire_brute = self.charger_grammaire()
        self.initialiser_regles()

        self.terminaux = []
        self.non_terminaux = []

        self.identifications_non_terminaux()

        print(self.terminaux)
        print(self.non_terminaux)

    def identifications_non_terminaux(self):
        for line in self.manager.ensemble_regles:
             self.non_terminaux += line.regle_decoupee[0]
             self.terminaux += line.regle_decoupee[1].split(' ')
        self.terminaux = [element for element in self.terminaux if element!='' and element not in self.non_terminaux]
        self.non_terminaux = [element for element in self.non_terminaux if element !=' ']


    def charger_regles(self):
        #on ouvre le fichier
        try:
            with open("rules.gramm","r") as file:
                data = file.readlines()
                # On lit les données et on retourne la grammaire
                self.grammaire_brute = [element.replace("\n","") for element in data]
                return self.grammaire_brute
        except:
            sys.stdout.write("Warning: Fichier input.gramm non trouvé.\nVoulez-vous tenter d'ouvrir un autre fichier?\n\nOuverture d'un autre fichier impossible dans l'état actuel des choses, désolé\n")
            exit()

    def charger_mots_cles():
        try:
            with open("words.gramm") as file:
                data=file.readlines()
            except:
                sys.stdout.write("Warning: Fichier input.gramm non trouvé.\nVoulez-vous tenter d'ouvrir un autre fichier?\n\nOuverture d'un autre fichier impossible dans l'état actuel des choses, désolé\n")
                exit()
    
    def charger_grammaire(self):
        return self.charger_regles()

    def initialiser_regles(self):
        self.manager = RegleManager.RegleManager(self.grammaire_brute)

    def __repr__(self):
        repr_str = "Grammaire\n\n"
        for regle in self.manager.ensemble_regles:
            repr_str += regle.__repr__()
        return repr_str
	            
if __name__=="__main__":
	grammaire = Grammaire()
	print(grammaire)
