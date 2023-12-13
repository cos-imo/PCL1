import Grammaire
import Regle

class RegleManager:

	ensemble_regles = []

	def __init__(self, ensemble_de_regles):
		self.ensemble_raw = ensemble_de_regles
		self.ensemble_regles = []
		self.initialiser_regles()
		self.premiers = {}
		self.suivants = {}
		self.ajouter_premier()
		print(self.premiers)
	
	def ajouter_regle(self, expression):
		if self.ensemble_regles == []:
			regle = Regle.Regle(0, expression)
			self.ensemble_regles.append(regle)
			self.ensemble_regles = list(set(self.ensemble_regles))
			return
		for regle in self.ensemble_regles:
			if ((regle.raw_regle) == expression):
				print("Doublon trouvé: " +expression)
				return
			else:
				regle = Regle.Regle(len(self.ensemble_regles), expression)
				self.ensemble_regles.append(regle)
				self.ensemble_regles = list(set(self.ensemble_regles))
				return
	
	def ajouter_premier(self):
		queue = []
		for regle in self.ensemble_regles:
			if (regle.membre_droit[0] not in self.premiers) and (regle.membre_droit[0].islower()):
				self.premiers[regle.membre_gauche.replace(" ","")] = regle.membre_droit[0].replace(" ","")
			else:
				if (regle.membre_gauche in self.premiers):
					self.premiers[regle.membre_gauche.replace(" ","")] += self.premiers[regle.membre_droit[0]]
				else:
					queue.append(regle)
			for element in queue:
				if regle.membre_droit[0] in self.premiers:
					self.premiers[element.membre_gauche.replace(" ","")] = self.premiers[regle.membre_droit[0]]
					queue.remove(element)
				else:
					print("Erreur: " + regle.membre_gauche + " n'a pas de premiers")
			
	
	def initialiser_regles(self):
		for regle in self.ensemble_raw:
			self.ajouter_regle(regle)
