import sys
import Regle

class Grammaire:
	def __init__(self):
		print("Grammaire initialisée")

    def charger_grammaire(self):
        with open("input.gramm","r") as file:
            data = file.readlines()
            grammaire_brute = [element.replace("\n","") for element in data]
            return grammaire_brute

if __name__=="__main__":
	grammaire = Grammaire()
