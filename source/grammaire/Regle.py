import sys
import math
import RegleManager

class Regle:

	def __init__(self, indice, expression):
		self.indice = indice+1
		self.membre_gauche = None
		self.membre_droit = None
		self.raw_regle = expression
		self.non_terminaux = []
		self.terminaux = []

		self.membre_gauche = self.decoupe_membre_gauche()
		self.membre_droit = self.decoupe_membre_droit()

		self.regle_decoupee = self.decoupe(expression)

		self.initialiser_non_terminaux()
		self.initialiser_terminaux()
		
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

	def decoupe_membre_droit(self):
		return [element for element in self.raw_regle.split("->")[1].split(" ") if element !='']

	def decoupe_membre_gauche(self):
		return self.raw_regle.split("->")[0]

	def __repr__(self):
		return "Regle\n\n\tExpresion: " + self.raw_regle + "\n\tPremiers: \n"
