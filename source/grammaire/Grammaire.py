import sys
import Regle
import RegleManager

class Grammaire:
	def __init__(self):
		self.grammaire_brute = self.charger_grammaire()
		self.initialiser_regles()

	def charger_grammaire(self):
	        try:
	            with open("./input.gramm","r") as file:
	                data = file.readlines()
	                self.grammaire_brute = [element.replace("\n","") for element in data]
	                return self.grammaire_brute
	        except:
	            sys.stdout.write("Warning: Fichier input.gramm non trouvé.\nVoulez-vous tenter d'ouvrir un autre fichier?\n\nOuverture d'un autre fichier impossible dans l'état actuel des choses, désolé\n")
	            exit()

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
