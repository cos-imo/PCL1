import sys
import modules.grammaire.Regle as Regle
import modules.grammaire.RegleManager as RegleManager
from automate import *
import copy
from graphviz import Digraph

class Grammaire:

    # ---------------------------------------------------------------------------------------------------------------
    # Section 1: Init
    # ---------------------------------------------------------------------------------------------------------------
    def __init__(self):

        self.axiome = None
        self.axiomeRegle = None

        self.keywords=[]
        self.grammaire_brute = self.charger_grammaire()
        self.initialiser_regles()

        self.mots_cles = []
        self.liste_mots = []

        self.terminaux = []
        self.non_terminaux = []

        self.terminaux = self.manager.get_terminaux()
        self.non_terminaux = self.manager.get_non_terminaux()

        self.premiers_non_terminaux = {}
        self.premiers_globaux = {}

        #Dictionnaire permettant de retrouver une règle depuis le premier élément de son membre droit
        self.regle_by_premier = {}

        self.suivants = {}

        self.ident = ["\n","+", "-", "*","/",":=","IDENT","cte","access", "and", "begin", "else", "elsif", "end","false", "for", "function", "if", "in", "is","loop", "new", "not", "null", "or", "out","procedure", "record", "rem", "return", "reverse", "then","true", "type", "use", "while", "with","]",":","(",")",",",";","=",".","'",">","<","str"]
        self.axiomeInt = None

        self.setRegleByPremier()
        #print(self.regle_by_premier)
        # self.setPremierNonTerminaux()
        # self.ajouter_premier_terminaux()
        #self.setObservers()
        
        self.setSuscribers()
        self.ajouter_premier_terminaux()
        #self.setPremierByNonTerminal()
        #self.clearPremiers()


        self.premiersDico = {}

        self.PremierDico()
        # self.set_premiers_regle()
        #self.calcul_suivants()
        self.premierToInt()
        # print(self.premiers_non_terminaux)
        self.RegleToInt()
        #print(self.suivants)

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
            with open("modules/grammaire/rules.gramm","r") as file:
                data = file.readlines()
                # On lit les données et on retourne la grammaire
                self.grammaire_brute = [element.replace("\n","") for element in data]
                self.axiome = self.grammaire_brute[0].split(" ->")[0]
                return self.grammaire_brute
        except:
            sys.stdout.write("Warning: Fichier input.gramm non trouvé.\nVoulez-vous tenter d'ouvrir un autre fichier?\n\nOuverture d'un autre fichier impossible dans l'état actuel des choses, désolé\n")
            exit()

    def charger_mots_cles(self):
        """
        Cette fonction ouvre le fichier words.gramm pour charger les mots-clés
        """
        try:
            with open("modules/grammaire/words.gramm") as file:
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
        self.manager = RegleManager.RegleManager(self.grammaire_brute, self.liste_mots, self)

    def charger_mots(self):
        """
        Cette fonction charge tout les mots du fichier grammaire. On pourra ensuite s'en servir, par exemple pour identifier les terminaux et les non terminaux
        """
        lst_temp = [element.replace("-> ","") for element in self.grammaire_brute]
        self.liste_mots = []
        for line in lst_temp:
            self.liste_mots += [element for element in line.split(" ")]
        self.liste_mots = list(set(self.liste_mots))

    def setRegleByPremier(self):
        for regle in self.manager.ensemble_regles:
            if regle.membre_gauche not in self.regle_by_premier:
                self.regle_by_premier[regle.membre_gauche] = [regle]
            else:
                self.regle_by_premier[regle.membre_gauche].append(regle)

    def setSuscribers(self):
        for regle in self.manager.ensemble_regles:
            if regle.membre_droit[0] not in self.non_terminaux:
                pass
            else:
                for regle_sus in self.regle_by_premier[regle.membre_droit[0]]:
                    regle_sus.addSuscriber(regle)

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
    # Section 5: Fonctions liées au premiers
    # ---------------------------------------------------------------------------------------------------------------

    def setObservers(self):
        for regle in self.manager.ensemble_regles:
            if regle.membre_droit[0] in self.non_terminaux:
                for regle_premier in self.regle_by_premier[regle.membre_droit[0]]:
                    regle_premier.addSuscriber(regle)

    def ajouter_premier_terminaux(self):
        """
        Calcule les premiers de chaque terminal
        """
        #On parcourt les règles
        for regle in self.manager.ensemble_regles:
            if self.est_terminal(regle.membre_droit[0]):
                regle.set_premier_regle(regle.membre_droit[0])
                regle.notifySuscribers(regle.membre_droit[0])
                if regle.membre_gauche in self.premiers_non_terminaux:
                    self.premiers_non_terminaux[regle.membre_gauche].append(regle.membre_droit[0])
                else:
                    self.premiers_non_terminaux[regle.membre_gauche] = [regle.membre_droit[0]]

    # def ajouter_premier(self, premier, non_terminal):
    #     if non_terminal not in self.premiers_non_terminaux:
    #         self.premiers_non_terminaux[non_terminal] = [premier]
    #     else:
    #         self.premiers_non_terminaux[non_terminal] += premier
    
    # def setPremierNonTerminaux(self):
    #     for regle in self.manager.ensemble_regles:
    #         if regle.membre_gauche not in self.premiers_non_terminaux:
    #             self.premiers_non_terminaux[regle.membre_gauche] = regle.premier
    #         else:
    #             for premier in regle.premier:
    #                 self.premiers_non_terminaux[regle.membre_gauche].append(premier)
    #                 self.premiers_non_terminaux[regle.membre_gauche] = list(set(self.premiers_non_terminaux[regle.membre_gauche]))
	
    # ---------------------------------------------------------------------------------------------------------------
    # Section 6: Fonctions liées aux suivants
    # ---------------------------------------------------------------------------------------------------------------
                
    def ajouter_suivants(self, element, suivants):
        """
        Ajoute les suivants donnés en argument au dictionnaire
        """
        if not (element in self.suivants):
            if isinstance(suivants, list):
                self.suivants[element] = suivants
            else:
                self.suivants[element] = [suivants]
        else:
            if isinstance(suivants, list):
                self.suivants[element] += suivants
            else:
                self.suivants[element] += [suivants]

    def calcul_suivants(self):
        """
        Calcule l'ensemble des suivants
        """
        queue=[]
        for regle in self.manager.ensemble_regles:
            for i in range(len(regle.membre_droit)-1):
                if regle.membre_droit[i+1] in self.terminaux:
                    self.ajouter_suivants(regle.membre_droit[i], regle.membre_droit[i+1])
                elif regle.membre_droit[i+1] in self.suivants:
                    self.ajouter_suivants(regle.membre_droit[i], self.premiers_terminaux[regle.membre_droit[i+1]])
                else:
                    queue.append((regle.membre_droit[i], regle.membre_droit[i+1]))
                    string = ""
                    for element in queue:
                        string += '(' + element[0] + ',' + element[1] + '),'
                    print("Erreur : " + string)
            if regle.membre_gauche in self.suivants:
                self.ajouter_suivants(regle.membre_droit[-1], self.suivants[regle.membre_gauche.replace(" ","")])
            else:
                queue.append((regle.membre_droit[-1], regle.membre_gauche.replace(" ","")))
        for j in range(len(queue)):
            for (element_a_ajouter, suivants_a_ajouter) in queue:
                if suivants_a_ajouter in self.suivants:
                    self.ajouter_suivants(element_a_ajouter, self.suivants[suivants_a_ajouter])
        for element in self.suivants:
            self.suivants[element] = list(set(self.suivants[element]))
        self.ajouter_suivants(self.axiome, ['$'])
    
    def premierToInt(self):
        for entry in self.premiers_non_terminaux:
            automate = Automate()
            self.premiers_non_terminaux[entry] = [automate.est_accepte(element) for element in self.premiers_non_terminaux[entry]]

    def RegleToInt(self):
        for regle in self.manager.ensemble_regles:
            automate = Automate()
            regleInt = automate.est_accepte(regle.raw_regle)
            regle.setRegleInt(regleInt[0][2:])
            if regle.raw_regle.split(" ")[0] == "FICHIER":
                self.axiomeInt = regle.RegleInt
                self.axiomeRegle = regle

    def PremierDico(self):
        for regle in self.manager.ensemble_regles:
            for element in self.premiers_non_terminaux[regle.membre_gauche]:
                if element not in self.premiersDico:
                    self.premiersDico[element] = [regle]
                else:
                    self.premiersDico[element].append(regle)
                    
if __name__=="__main__":
    grammaire = Grammaire()
