import sys
import modules.grammaire.Regle as Regle
import modules.grammaire.RegleManager as RegleManager
import copy

class Grammaire:

    # ---------------------------------------------------------------------------------------------------------------
    # Section 1: Init
    # ---------------------------------------------------------------------------------------------------------------
    def __init__(self):
        self.keywords=[]
        self.grammaire_brute = self.charger_grammaire()
        self.initialiser_regles()

        self.mots_cles = []
        self.liste_mots = []

        self.terminaux = []
        self.non_terminaux = []

        self.terminaux = self.manager.get_terminaux()
        self.non_terminaux = self.manager.get_non_terminaux()

        self.premiers_terminaux = {}

        self.ajouter_premier_terminaux()
        self.set_premiers_regle()

    # ---------------------------------------------------------------------------------------------------------------
    # Section 2: Chargement
    # ---------------------------------------------------------------------------------------------------------------

    def charger_grammaire(self):
        """
        Cette fonction appelle les différentes fonctions de chargement, en l'occurence
         * charger_regles()
        et
         * charger_mots_cles()
        """
        self.charger_mots_cles()
        return self.charger_regles()

    def charger_regles(self):
        """
        Cette fonction ouvre le fichier 'rules.gramm' pour charger les règles
        """
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
        """
        Cette fonction ouvre le fichier words.gramm pour charger les mots-clés
        """
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


    # ---------------------------------------------------------------------------------------------------------------
    # Section 2: Coeur de la grammaire
    # ---------------------------------------------------------------------------------------------------------------
    def initialiser_regles(self):
        self.charger_mots()
        self.manager = RegleManager.RegleManager(self.grammaire_brute, self.liste_mots)

    def charger_mots(self):
        """
        Cette fonction charge tout les mots du fichier grammaire. On pourra ensuite s'en servir, par exemple pour identifier les terminaux et les non terminaux
        """
        lst_temp = [element.replace("-> ","") for element in self.grammaire_brute]
        self.liste_mots = []
        for line in lst_temp:
            self.liste_mots += [element for element in line.split(" ")]
        self.liste_mots = list(set(self.liste_mots))


    # ---------------------------------------------------------------------------------------------------------------
    # Section 4: Fonctions utilitaires
    # ---------------------------------------------------------------------------------------------------------------

    def __repr__(self):
        """
        Cette  fonction définit la présentation de notre objet
        """
        repr_str = "Grammaire\n\n"
        for regle in self.manager.ensemble_regles:
            repr_str += regle.__repr__() + "\n"
        return repr_str

    def est_terminal(self, element):
        """
        Cette fonction permet de tester si un élément est contenu dans la liste des terminaux
        """
        return (element in self.terminaux)
    
    def affiche(self):
        print(self)
    
    # ---------------------------------------------------------------------------------------------------------------
    # Section 4: Fonctions dépréciées/en cours de code
    # --------------------------------------------------------------------------------------------------------------

    def ajouter_premier_terminaux(self):
        """
        Calcule les premiers de chaque terminal
        """
        queue = []
        #On parcourt les règles
        for regle in self.manager.ensemble_regles:
            if self.est_terminal(regle.premier):
                # Si le premier élément est un terminal
                if regle.membre_gauche not in self.premiers_terminaux:
                    # Si la liste des premiers associée n'existe pas dans le dictionnaire, on la créée
                    self.premiers_terminaux[regle.membre_gauche.replace(" ","")] = regle.premier
                else:
                    # Sinon, on se contente de l'ajouter à la liste existante
                    self.premiers_terminaux[regle.membre_gauche.replace(" ","")] += regle.premier
            else:
                # Sinon, si le premier élément n'est pas un terminal
                if regle.premier in self.premiers_terminaux:
                    # Si les premiers du non-terminal existe:
                    if regle.membre_gauche not in self.premiers_terminaux:
                        # Si la liste des premiers associée n'existe pas dans le dictionnaire, on l'initialise en ajoutant la liste des premiers du permier non terminal de la partie droite
                        self.premiers_terminaux[regle.membre_gauche.replace(" ","")] = self.premiers_terminaux[regle.premier]
                    else:
                        # Sinon, on ajoute lesdits premiers à la liste des premiers
                        self.premiers_terminaux[regle.membre_gauche.replace(" ","")] += self.premiers_terminaux[regle.premier]
                else:
                    # Si la liste des premiers n'existe pas, on ajoute la règle à la file d'attente 
                    queue.append(regle)

        for i in range(len(queue)):
            for regle in queue:
                if regle.premier in self.premiers_terminaux:
                    # Si les premiers ont été calculés, on les ajoute
                    self.premiers_terminaux[regle.membre_gauche.replace(" ","")] = self.premiers_terminaux[regle.premier]
                    queue.remove(regle)
                    
        for regle in queue:
            # On parcourt une denière fois la liste d'attente
            if regle.premier in self.premiers_terminaux:
                self.premiers_terminaux[regle.membre_gauche.replace(" ","")] = self.premiers_terminaux[regle.premier]
                queue.remove(regle)
            else:
                # Si on a finalement rien trouvé, on renvoie un message d'erreur
                print("Erreur: " + regle.membre_gauche + " n'a pas de premiers.\n Vérifiez votre grammaire.")

    def set_premiers_regle(self):
        for regle in self.manager.ensemble_regles:
            if regle.membre_droit[0] in self.terminaux:
                regle.set_premier_regle(regle.premier)
            elif regle.membre_droit[0] in self.premiers_terminaux:
                regle.set_premier_regle(self.premiers_terminaux[regle.premier])
            else:
                print("Erreur: premier non trouvé: ")
                print(regle.membre_droit[0])
                print(self.premiers_terminaux)
                exit()
	


if __name__=="__main__":
    grammaire = Grammaire()
    grammaire.affiche()