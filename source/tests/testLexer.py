from token_analyser import *
from token_generator import *
from arguments import Parser
import sys

parser=Parser()
data=parser.args.sourcefile.readlines()

analyseur = tokeniser_t()
tokens=analyseur.tokenise_file(data)

print(tokens)