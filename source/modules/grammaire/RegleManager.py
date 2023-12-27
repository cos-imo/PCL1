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
            # Si aucune règle n'a encore été initialisée (la liste n'existe donc pas encore), on crée la règle et on l'ajoute
			regle = Regle.Regle(0, expression, self.premiers_terminaux)
			self.ensemble_regles.append(regle)
			self.ensemble_regles = list(set(self.ensemble_regles))
			return
		for regle in self.ensemble_regles:
			if ((regle.raw_regle) == expression):
                # Si la règle à déjà ete vue, on renvoie un message (mais on continue l'éxecution)
				print("Doublon trouvé: " + expression)
				return
			else:
                # Sinon on initialise un objet Regle
				regle = Regle.Regle(len(self.ensemble_regles), expression, self.premiers_terminaux)
                # Et on l'ajoute en supprimant les doublons
				self.ensemble_regles.append(regle)
				self.ensemble_regles = list(set(self.ensemble_regles))
				return
	
	def ajouter_premier_terminaux(self):
        """
        Calcule les premiers de chaque terminal
        """
		queue = []
        #On parcourt les règles
		for regle in self.ensemble_raw:
            #On découpe chaque règle
			partie_droite = regle.split("->")[1][1:].split(" ")
			partie_gauche = regle.split("->")[0].replace(" ","")
			if partie_droite[0].islower():
                # Si le premier élément est en minuscule (il s'agit donc d'un terminal)
				if partie_gauche not in self.premiers_terminaux:
                    # Si la liste des premiers associée n'existe pas dans le dictionnaire, on la créée
					self.premiers_terminaux[partie_gauche] = partie_droite[0]
				else:
                    # Sinon, on se contente de l'ajouter à la liste existante
					self.premiers_terminaux[partie_gauche] += partie_droite[0]
			else:
                # Sinon, si le premier élément n'est pas un terminal
				if partie_droite[0] in self.premiers_terminaux:
                    # Si les premiers du non-terminal existe:
					if regle.partie_gauche not in self.premiers_terminaux:
                        # Si la liste des premiers associée n'existe pas dans le dictionnaire, on l'initialise en ajoutant la liste des premiers du permier non terminal de la partie droite
						self.premiers_terminaux[partie_gauche] = self.premiers_terminaux[partie_droite[0]]
					else:
                        # Sinon, on ajoute lesdits premiers à la liste des premiers
						self.premiers_terminaux[partie_gauche] += self.premiers_terminaux[partie_droite[0]]
				else:
                    # Si la liste des premiers n'existe pas, on ajoute la règle à la file d'attente 
					queue.append(regle)

		for i in range(len(queue)):
			for element in queue:
                # On parcourt les règles et on les découpe
				partie_droite = element.split("->")[1][1:].split(" ")
				partie_gauche = element.split("->")[0].replace(" ","")
				if partie_droite[0] in self.premiers_terminaux:
                    # Si les premiers ont été calculés, on les ajoute
					self.premiers_terminaux[partie_gauche] = self.premiers_terminaux[partie_droite[0]]
					queue.remove(element)

		for element in queue:
            # On parcourt une denière fois la liste d'attente
			partie_droite = element.split("->")[1][1:].split(" ")
			partie_gauche = element.split("->")[0].replace(" ","")
			if partie_droite[0] in self.premiers_terminaux:
				self.premiers_terminaux[partie_gauche] = self.premiers_terminaux[partie_droite[0]]
				queue.remove(element)
			else:
                # Si on a finalement rien trouvé, on renvoie un message d'erreur
				print("Erreur: " + partie_gauche + " n'a pas de premiers.\n Vérifiez votre grammaire.")

			
	
	def initialiser_regles(self):
        """
        Appelle self.ajoute_regle pour chaque règle contenue dans le fichier
        """
		for regle in self.ensemble_raw:
			self.ajouter_regle(regle)
