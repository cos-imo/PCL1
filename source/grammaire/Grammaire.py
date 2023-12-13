import sys
import Regle

class Grammaire:
	def __init__(self):
		self.grammaire_brute = self.charger_grammaire()
		self.grammaire_decoupee = self.decoupe(self.grammaire_brute)
		self.non_terminaux = []
		self.terminaux = []
		self.initialiser_non_terminaux()
		print(self.non_terminaux)

	def charger_grammaire(self):
	        try:
	            with open("input.gramm","r") as file:
	                data = file.readlines()
	                grammaire_brute = [element.replace("\n","") for element in data]
	                return grammaire_brute
	        except:
	            sys.stdout.write("Warning: Fichier input.gramm non trouvé.\nVoulez-vous tenter d'ouvrir un autre fichier?\n\nOuverture d'un autre fichier impossible dans l'état 	actuel des choses, désolé\n")
	            exit()
	            
	def decoupe(self, grammaire_brute):
		grammaire_decoupee = []
		for line in grammaire_brute:
			grammaire_decoupee.append(line.split(" -> "))
		return grammaire_decoupee

	def initialiser_non_terminaux(self):
		for line in self.grammaire_decoupee:
			self.non_terminaux.append(line[0])
			self.non_terminaux += [char for char in line[1].split(" ") if char.isupper()]
			self.non_terminaux = list(set(self.non_terminaux))


if __name__=="__main__":
	grammaire = Grammaire()
