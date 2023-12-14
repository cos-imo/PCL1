import Grammaire
import Regle

class RegleManager:

	ensemble_regles = []

	def __init__(self, ensemble_de_regles):
		self.ensemble_raw = ensemble_de_regles

		self.premiers_terminaux = {}
		self.suivants = {}

		self.ensemble_regles = []
		self.initialiser_regles()
		self.ajouter_premier_terminaux()
		print(self.premiers_terminaux)
	
	def ajouter_regle(self, expression):
		if self.ensemble_regles == []:
			regle = Regle.Regle(0, expression, self.premiers_terminaux)
			self.ensemble_regles.append(regle)
			self.ensemble_regles = list(set(self.ensemble_regles))
			return
		for regle in self.ensemble_regles:
			if ((regle.raw_regle) == expression):
				print("Doublon trouvé: " + expression)
				return
			else:
				regle = Regle.Regle(len(self.ensemble_regles), expression, self.premiers_terminaux)
				self.ensemble_regles.append(regle)
				self.ensemble_regles = list(set(self.ensemble_regles))
				return
	
	def ajouter_premier_terminaux(self):
		queue = []
		for regle in self.ensemble_raw:
			partie_droite = regle.split("->")[1][1:].split(" ")
			partie_gauche = regle.split("->")[0].replace(" ","")
			if partie_droite[0].islower():
				if partie_gauche not in self.premiers_terminaux:
					self.premiers_terminaux[partie_gauche] = partie_droite[0]
				else:
					self.premiers_terminaux[partie_gauche] += partie_droite[0]
			else:
				if partie_droite[0] in self.premiers_terminaux:
					if regle.partie_gauche not in self.premiers_terminaux:
						self.premiers_terminaux[partie_gauche] = self.premiers_terminaux[partie_droite[0]]
					else:
						self.premiers_terminaux[partie_gauche] += self.premiers_terminaux[partie_droite[0]]
				else:
					queue.append(regle)

		for i in range(len(queue)):
			for element in queue:
				partie_droite = element.split("->")[1][1:].split(" ")
				partie_gauche = element.split("->")[0].replace(" ","")
				if partie_droite[0] in self.premiers_terminaux:
					self.premiers_terminaux[partie_gauche] = self.premiers_terminaux[partie_droite[0]]
					queue.remove(element)
		for element in queue:
			partie_droite = element.split("->")[1][1:].split(" ")
			partie_gauche = element.split("->")[0].replace(" ","")
			if partie_droite[0] in self.premiers_terminaux:
				self.premiers_terminaux[partie_gauche] = self.premiers_terminaux[partie_droite[0]]
				queue.remove(element)
			else:
				print("Erreur: " + partie_gauche + " n'a pas de premiers.\n Vérifiez votre grammaire.")

			
	
	def initialiser_regles(self):
		for regle in self.ensemble_raw:
			self.ajouter_regle(regle)
