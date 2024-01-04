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

		self.premier = None

		self.decoupe(self.raw_regle)

		self.init_premier()
		

    # ---------------------------------------------------------------------------------------------------------------
    # Section 2: Fonctions utilitaires
    # ---------------------------------------------------------------------------------------------------------------
		
	def decoupe(self, regle_brute):
		self.regle_brute_decoupee = regle_brute.split("->")
		self.decoupe_membre_droit()
		self.decoupe_membre_gauche()

	def decoupe_membre_droit(self):
		self.membre_droit = [element for element in self.regle_brute_decoupee[1].split(" ") if element!='']

	def decoupe_membre_gauche(self):
		self.membre_gauche = self.regle_brute_decoupee[0]


    # ---------------------------------------------------------------------------------------------------------------
    # Section 3: Fonctions utilitaires: Getter et Setter
    # ---------------------------------------------------------------------------------------------------------------

	def get_membre_gauche(self):
		return self.membre_gauche
	
	def get_membre_droit(self):
		return self.membre_droit
	
	def set_premier_regle(self, premier):
		self.premier = premier

	def init_premier(self):
		self.premier = self.membre_droit[0]


    # ---------------------------------------------------------------------------------------------------------------
    # Section 4: Fonctions utilitaires: Représentation
    # ---------------------------------------------------------------------------------------------------------------
				
	def __repr__(self):
		membre_droit_str = ""
		for element in self.membre_droit:
			membre_droit_str += element + " "
		return "Regle\n\n\tExpresion: " + self.raw_regle + "\n\t\tMembre gauche: " + self.membre_gauche + "\n\t\tMembre droit: " + membre_droit_str + "\n\t\tPremier: " + self.premier
