import sys
import math
import RegleManager

class Regle:

	def __init__(self, indice, expression, premier_terminaux):
		self.indice = indice+1
		
		self.membre_gauche = None
		self.membre_droit = None
		
		self.raw_regle = expression

		self.non_terminaux = []
		self.terminaux = []

		self.membre_gauche = self.decoupe_membre_gauche()
		self.membre_droit = self.decoupe_membre_droit()

		self.regle_decoupee = self.decoupe(expression)

		self.premiers_terminaux = premier_terminaux
		self.premiers = []
		self.suivants = []

		#self.ajouter_premier()

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
	
	"""
	def ajouter_premier(self):
		if self.membre_droit[0].islower():
			self.premiers.append(self.membre_droit[0])
		else:
			if self.membre_droit[0] in self.premiers_terminaux:
				self.premiers.append(self.premiers_terminaux[self.membre_droit[0]])
			else:
				print("Erreur: premier non trouvé : " + self.raw_regle)
				exit()
	"""
				
	def __repr__(self):
		premiers_str = ""
		for premier in self.premiers:
			premiers_str += "\t" + premier
		return "Regle\n\n\tExpresion: " + self.raw_regle + "\n\tPremiers: \n" + premiers_str
