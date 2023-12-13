import sys
import math

class Regle:

	def __init__(self, indice, expression):
		self.indice = indice+1
		self.membre_gauche = None
		self.membre_droit = None
		self.raw_regle = expression
		self.non_terminaux = []
		self.terminaux = []

		self.regle_decoupee = self.decoupe(expression)

		self.initialiser_non_terminaux()
		self.initialiser_terminaux()
		sys.stdout.write("Création de la règle\n")
		
	def decoupe(self, regle_brute):
		return regle_brute.split("->")

	def initialiser_non_terminaux(self):
		for line in self.regle_decoupee:
			self.non_terminaux.append(line[0])
			self.non_terminaux += [char for char in line[1].split(" ") if char.isupper()]
			self.non_terminaux = list(set(self.non_terminaux))

	def initialiser_terminaux(self):
		for line in self.regle_decoupee:
			self.terminaux += [char for char in line[1].split(" ") if char.islower()]
			self.terminaux = list(set(self.terminaux))

	def __repr__(self):
		return "Regle\n\n\tExpresion: " + self.raw_regle + "\n\tPremiers: "
