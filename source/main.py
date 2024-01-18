from automate import *
from arguments import Parser 
from export import * 
from token_analyser import *
from token_generator import *
from error_handler import *
from grammaire import *
from analyzer import *
import sys, os

parser=Parser()

data=parser.args.sourcefile.read()

"""
token_analyser = tokeniser_t()

if parser.args.verbose:
    verbose_mode = parser.args.verbose   
    token_analyser.verbose(data, verbose_mode)
else:
    sys.stdout.write("mode verbose: désactivé\n")
    token_list=token_analyser.est_accepte(data)
    sys.stdout.write("Fichier compilé\n")

if parser.args.create_dump:
   sys.stdout.write("Création du fichier dump\n")
   exporter=data_exporter()
   token_list=token_analyser.codage_token(data)
   dump_mode=parser.args.create_dump
   print(parser.args.create_dump)
   exporter.create_dump_file(token_list, dump_mode)
"""

automate = Automate()
automate.est_accepte(data)
if automate.etat_comp:
    grammaire = Grammaire.Grammaire()
    print(automate.table_idf)
    if parser.args.tree:
        if parse_syntax(automate, grammaire, True):
            print("Analyse syntaxique réussie")
        else:
            print("L'analyse syntaxique à échoué")
            print(automate.liste_token)
    else:
        if parse_syntax(automate, grammaire):
            print("Analyse syntaxique réussie")
        else:
            print("L'analyse syntaxique à échoué")
            print(automate.liste_token)
else:
    automate.print_error()

# res = main(data)

# print(res)

# grammaire = Grammaire.Grammaire()

# print(grammaire.premiersDico)

# axiome = grammaire.axiomeRegle.RegleInt[1:]

# currentRule = axiome

# print(axiome)