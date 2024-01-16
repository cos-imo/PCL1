from automate import *
from arguments import Parser 
from export import * 
from token_analyser import *
from token_generator import *
from error_handler import *
from grammaire import *
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

res = main(data)

print(res)

grammaire = Grammaire.Grammaire()

axiome = grammaire.axiomeRegle.RegleInt[1:]

currentRule = axiome

print(axiome)