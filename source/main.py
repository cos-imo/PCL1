from token_analyser import *
from token_generator import *
from arguments import args
import sys, os

data=args.sourcefile.readlines()
token_analyser_instance = tokeniser_t()

if args.verbose:
    token_analyser_instance.verbose(data)
