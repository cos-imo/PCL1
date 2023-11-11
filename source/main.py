from token_analyser import *
from token_generator import *
from arguments import Parser 
import sys, os

parser=Parser()

data=parser.args.sourcefile.readlines()
token_analyser = tokeniser_t()

if parser.args.verbose:
    verbose_mode = parser.args.verbose   
    token_analyser.verbose(data, verbose_mode)
else:
    sys.stdout.write("mode verbose: désactivé\n")
    token_list=token_analyser.tokenise_file(data)
    sys.stdout.write("Fichier compilé\n")
