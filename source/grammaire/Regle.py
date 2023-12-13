import sys
import math

class Regle:

	def __init__(self):
		self.indice = math.inf
		self.membre_gauche = None
		self.membre_droit = None
		self.raw_regle = ""
		self.non_terminaux = []
		self.terminaux = []
		self.initialiser_non_terminaux()
		self.initialiser_terminaux()
		sys.stdout.write("Création de la règle\n")
		
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

	def initialiser_terminaux(self):
		for line in self.grammaire_decoupee:
			self.terminaux += [char for char in line[1].split(" ") if char.islower()]
			self.terminaux = list(set(self.terminaux))
