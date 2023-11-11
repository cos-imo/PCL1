from token_analyser import *
from token_generator import *
from arguments import Parser 
import sys, os

parser=Parser()

data=parser.args.sourcefile.readlines()
token_analyser_instance = tokeniser_t()

if parser.args.verbose:
    token_analyser_instance.verbose(data)
