import sys
import math
import modules.grammaire.RegleManager

class Regle:

    # ---------------------------------------------------------------------------------------------------------------
    # Section 1: Init
    # ---------------------------------------------------------------------------------------------------------------
	def __init__(self, indice, expression):
		self.indice = indice+1
		
		self.membre_gauche = None
		self.membre_droit = None
		
		self.raw_regle = expression

		self.non_terminaux = []
		self.terminaux = []

		self.regle_brute_decoupee = self.decoupe(self.raw_regle)
		

	def decoupe(self, regle_brute):
		return regle_brute.split("->")

	def decoupe_membre_droit(self):
		self.membre_droit = self.regle_brute_decoupee[1]

	def decoupe_membre_gauche(self):
		self.membre_gauche = self.regle_brute_decoupee[0]
				
	def __repr__(self):
		return "Regle\n\n\tExpresion: " + self.raw_regle
