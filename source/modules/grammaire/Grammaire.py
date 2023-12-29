import sys
import Regle
import RegleManager

class Grammaire:
    def __init__(self):
        self.grammaire_brute = self.charger_grammaire()
        self.initialiser_regles()

        self.mots_cles = []

        self.terminaux = []
        self.non_terminaux = []

        self.keywords=[]

        self.identifications_non_terminaux()

        #print(self.terminaux)
        #print(self.non_terminaux)

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

    def charger_mots_cles(self):
        try:
            with open("words.gramm") as file:
                data=file.readlines()
                if "[" in data[0]:
                    data[0] = data[0].split("[")[1]
                data = data[:-1]
                formatted_data = [element.replace("\n","").replace("\"","").replace("'","").replace("  ","").split(",") for element in data]
                data=[]
                for element in formatted_data:
                    data = [el.replace(" ","") for el in data + element if ((el!='') and (el!=' '))]
                self.keywords=data
        except:
            sys.stdout.write("Warning: Fichier words.gramm non trouvé.\nVoulez-vous tenter d'ouvrir un autre fichier?\n\nOuverture d'un autre fichier impossible dans l'état actuel des choses, désolé\n")
            exit()
    
    def charger_grammaire(self):
        self.charger_mots_cles()
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
	#print(grammaire)
