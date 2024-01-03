import sys
import Regle
import RegleManager
import copy

class Grammaire:
    def __init__(self):
        self.keywords=[]
        self.grammaire_brute = self.charger_grammaire()
        self.initialiser_regles()

        self.mots_cles = []

        self.terminaux = []
        self.non_terminaux = []

        self.identifications_non_terminaux()

    def identifications_non_terminaux(self):
        for line in self.manager.ensemble_regles:
             self.non_terminaux += line.regle_decoupee[0]
             self.terminaux += line.regle_decoupee[1].split(' ')
        self.terminaux = [element for element in self.terminaux if element!='' and element not in self.non_terminaux]
        self.non_terminaux = [element for element in self.non_terminaux if element !=' ']


    def charger_regles(self):
        #on ouvre le fichier
        try:
            with open("rules.gramm","r") as file:
                data = file.readlines()
                # On lit les données et on retourne la grammaire
                self.grammaire_brute = [element.replace("\n","") for element in data]
                return self.grammaire_brute
        except:
            sys.stdout.write("Warning: Fichier input.gramm non trouvé.\nVoulez-vous tenter d'ouvrir un autre fichier?\n\nOuverture d'un autre fichier impossible dans l'état actuel des choses, désolé\n")
            exit()

    def charger_mots_cles(self):
        try:
            with open("words.gramm") as file:
                data=file.readlines()
                if "[" in data[0]:
                    data[0] = data[0].split("[")[1]
                data = data[:-1]
                formatted_data = [element.replace("\n","").replace("\"","").replace("'","").replace("  ","").split(",") for element in data]
                data=[]
                for element in formatted_data:
                    data = [el.replace(" ","") for el in data + element if ((el!='') and (el!=' '))]
                self.keywords=copy.deepcopy(data)
        except:
            sys.stdout.write("Warning: Fichier words.gramm non trouvé.\nVoulez-vous tenter d'ouvrir un autre fichier?\n\nOuverture d'un autre fichier impossible dans l'état actuel des choses, désolé\n")
            exit()
    
    def charger_grammaire(self):
        self.charger_mots_cles()
        return self.charger_regles()

    def initialiser_regles(self):
        self.manager = RegleManager.RegleManager(self.grammaire_brute)

    def __repr__(self):
        repr_str = "Grammaire\n\n"
        for regle in self.manager.ensemble_regles:
            repr_str += regle.__repr__()
        return repr_str

    def est_terminal(self, element):
        return (element in self.terminaux)
    
    # def ajouter_premier_terminaux(self):
	# 	"""
    #     Calcule les premiers de chaque terminal
    #     """
	# 	queue = []
    #     #On parcourt les règles
	# 	for regle in self.ensemble_raw:
    #         #On découpe chaque règle
	# 		partie_droite = regle.split("->")[1][1:].split(" ")
	# 		partie_gauche = regle.split("->")[0].replace(" ","")
	# 		if self.est_terminal(partie_droite[0]):
    #             # Si le premier élément est en minuscule (il s'agit donc d'un terminal)
	# 			if partie_gauche not in self.premiers_terminaux:
    #                 # Si la liste des premiers associée n'existe pas dans le dictionnaire, on la créée
	# 				self.premiers_terminaux[partie_gauche] = partie_droite[0]
	# 			else:
    #                 # Sinon, on se contente de l'ajouter à la liste existante
	# 				self.premiers_terminaux[partie_gauche] += partie_droite[0]
	# 		else:
    #             # Sinon, si le premier élément n'est pas un terminal
	# 			if partie_droite[0] in self.premiers_terminaux:
    #                 # Si les premiers du non-terminal existe:
	# 				if regle.partie_gauche not in self.premiers_terminaux:
    #                     # Si la liste des premiers associée n'existe pas dans le dictionnaire, on l'initialise en ajoutant la liste des premiers du permier non terminal de la partie droite
	# 					self.premiers_terminaux[partie_gauche] = self.premiers_terminaux[partie_droite[0]]
	# 				else:
    #                     # Sinon, on ajoute lesdits premiers à la liste des premiers
	# 					self.premiers_terminaux[partie_gauche] += self.premiers_terminaux[partie_droite[0]]
	# 			else:
    #                 # Si la liste des premiers n'existe pas, on ajoute la règle à la file d'attente 
	# 				queue.append(regle)

	# 	for i in range(len(queue)):
	# 		for element in queue:
    #             # On parcourt les règles et on les découpe
	# 			partie_droite = element.split("->")[1][1:].split(" ")
	# 			partie_gauche = element.split("->")[0].replace(" ","")
	# 			if partie_droite[0] in self.premiers_terminaux:
    #                 # Si les premiers ont été calculés, on les ajoute
	# 				self.premiers_terminaux[partie_gauche] = self.premiers_terminaux[partie_droite[0]]
	# 				queue.remove(element)

	# 	for element in queue:
    #         # On parcourt une denière fois la liste d'attente
	# 		partie_droite = element.split("->")[1][1:].split(" ")
	# 		partie_gauche = element.split("->")[0].replace(" ","")
	# 		if partie_droite[0] in self.premiers_terminaux:
	# 			self.premiers_terminaux[partie_gauche] = self.premiers_terminaux[partie_droite[0]]
	# 			queue.remove(element)
	# 		else:
    #             # Si on a finalement rien trouvé, on renvoie un message d'erreur
	# 			print("Erreur: " + partie_gauche + " n'a pas de premiers.\n Vérifiez votre grammaire.")	
	


if __name__=="__main__":
	grammaire = Grammaire()
