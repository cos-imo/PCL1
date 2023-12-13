import Grammaire
import Regle

class RegleManager:
	def __init__(self, ensemble_de_regles):
		self.ensemble_raw = ensemble_de_regles
		self.ensemble_regles = []
		self.initialiser_regles()
	
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
				print(regle)
				print(self.ensemble_regles)
				return
	
	def initialiser_regles(self):
		for regle in self.ensemble_raw:
			self.ajouter_regle(regle)
