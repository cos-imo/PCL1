import sys
import Regle

class Grammaire:
	def __init__(self):
        	self.charger_grammaire()
        	print("Grammaire initialisée")

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

if __name__=="__main__":
	grammaire = Grammaire()
