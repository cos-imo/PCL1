import modules.grammaire.Regle as Regle
import modules.grammaire.Grammaire as Grammaire

class RegleManager:

    # ---------------------------------------------------------------------------------------------------------------
    # Section 0: Définitions des variables globales
    # ---------------------------------------------------------------------------------------------------------------
	ensemble_regles = []
	

    # ---------------------------------------------------------------------------------------------------------------
    # Section 1: Init
    # ---------------------------------------------------------------------------------------------------------------
	def __init__(self, ensemble_de_regles, liste_mots, grammaire):
		self.ensemble_raw = ensemble_de_regles

		self.liste_mots = liste_mots
		self.non_terminaux = []
		self.terminaux = []
		self.suivants = {}

		self.ensemble_regles = []
		self.initialiser_regles(grammaire)
		self.set_non_terminaux()
		self.set_terminaux()
	

    # ---------------------------------------------------------------------------------------------------------------
    # Section 2: Management des règles
    # ---------------------------------------------------------------------------------------------------------------
		
	def ajouter_regle(self, expression, grammaire):
		if self.ensemble_regles == []:
            # Si aucune règle n'a encore été initialisée (la liste n'existe donc pas encore), on crée la règle et on l'ajoute
			regle = Regle.Regle(0, expression)
			regle.setManager(self)
			regle.setGrammaire(grammaire)
			self.ensemble_regles.append(regle)
			self.ensemble_regles = list(set(self.ensemble_regles))
			return
		for regle in self.ensemble_regles:
			if ((regle.raw_regle) == expression):
                # Si la règle à déjà été vue, on renvoie un message (mais on continue l'éxecution)
				print("Doublon trouvé: " + expression)
				return
			else:
                # Sinon on initialise un objet Regle
				regle = Regle.Regle(len(self.ensemble_regles), expression)
				regle.setManager(self)
				regle.setGrammaire(grammaire)
                # Et on l'ajoute en supprimant les doublons
				self.ensemble_regles.append(regle)
				self.ensemble_regles = list(set(self.ensemble_regles))
				return
			
	def initialiser_regles(self, grammaire):
		"""
        Appelle self.ajoute_regle pour chaque règle contenue dans le fichier
        """
		for regle in self.ensemble_raw:
			self.ajouter_regle(regle, grammaire)

    # ---------------------------------------------------------------------------------------------------------------
    # Section 3: Fonctions utilitaires: Getter et Setter
    # ---------------------------------------------------------------------------------------------------------------
	
	def get_ensemble_regles(self):
		return self.ensemble_regles
	
	def set_non_terminaux(self):
		for regle in self.ensemble_regles:
			self.non_terminaux += [regle.get_membre_gauche().replace(' ','')]
	
	def get_non_terminaux(self):
		return self.non_terminaux
	
	def set_terminaux(self):
		for mot in self.liste_mots:
			if not (mot in self.non_terminaux):
				self.terminaux += [mot]
	
	def get_terminaux(self):
		return self.terminaux
