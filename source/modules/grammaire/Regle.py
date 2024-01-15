import sys
import math
import RegleManager

class Regle:

    # ---------------------------------------------------------------------------------------------------------------
    # Section 1: Init
    # ---------------------------------------------------------------------------------------------------------------
	def __init__(self, indice, expression):
		self.indice = indice+1
		
		self.grammaire = None
		self.manager = None
		
		self.membre_gauche = None
		self.membre_droit = None
		
		self.raw_regle = expression

		self.non_terminaux = []
		self.terminaux = []

		self.premier = None
		self.suscribers = []

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
		self.membre_gauche = self.regle_brute_decoupee[0][:-1]


    # ---------------------------------------------------------------------------------------------------------------
    # Section 3: Fonctions utilitaires: Getter et Setter
    # ---------------------------------------------------------------------------------------------------------------

	def get_membre_gauche(self):
		return self.membre_gauche
	
	def get_membre_droit(self):
		return self.membre_droit
	
	def set_premier_regle(self, premier):
		if self.premier is None:
			self.premier = [premier]
		else:
			self.premier.append(premier)
			self.premier = list(set(self.premier))

	def init_premier(self):
		self.premier = [self.membre_droit[0]]

    # ---------------------------------------------------------------------------------------------------------------
    # Section 4: Fonctions utilitaires: Représentation
    # ---------------------------------------------------------------------------------------------------------------
				
	def __repr__(self):
		membre_droit_str = ""
		premier_str = ""
		for element in self.membre_droit:
			membre_droit_str += element + " "
		for premier in self.premier:
			premier_str += premier
		return "Regle\n\n\tExpresion: " + self.raw_regle + "\n\t\tMembre gauche: " + self.membre_gauche + "\n\t\tMembre droit: " + membre_droit_str + "\n\t\tPremier: " + premier_str

    # ---------------------------------------------------------------------------------------------------------------
    # Section 5: Observateurs
    # ---------------------------------------------------------------------------------------------------------------

	def addSuscriber(self, suscriber):
		self.suscribers.append(suscriber)
	
	def notifySuscribers(self, symbole):
		for suscriber in self.suscribers:
			suscriber.notify(symbole)
	
	def notify(self, symbole):
		self.set_premier_regle(symbole)
		self.notifySuscribers(symbole)
		if self.membre_gauche in self.grammaire.premiers_non_terminaux:
			self.grammaire.premiers_non_terminaux[self.membre_gauche].append(symbole)
		else:
			self.grammaire.premiers_non_terminaux[self.membre_gauche] = [symbole]



    # ---------------------------------------------------------------------------------------------------------------
    # Section 6: Ajout du manager et de la grammaire 
    # ---------------------------------------------------------------------------------------------------------------
	
	def setManager(self, manager):
		self.manager = manager
		
	def setGrammaire(self, grammaire):
		self.grammaire = grammaire
