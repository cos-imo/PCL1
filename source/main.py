from token_analyser import *
from token_generator import *
from arguments import args
import sys, os

"""
if len(sys.argv)!=2:
    sys.stdout.write("ERREUR\n")
    sys.stdout.write("\tUsage:\tpython3 source/main.py [nom_du_fichier]\n")
    sys.stdout.write("\t\t[nom_du_fichier] est le nom du fichier canAda à compiler\n")
    sys.stdout.write("\t\t\n")
else:
    if os.path.isfile(sys.argv[-1]):
        with open(sys.argv[-1], 'r') as file:
            data = file.readlines()
            verbose(data)
    else:
        sys.stdout.write("ERREUR\nCompilation impossible: Fichier canAda non trouvé\n")
"""

if len(sys.argv)==2:
    data=args.sourcefile.readlines()
    token_analyser_instance = tokeniser_t()
    token_analyser_instance.verbose(data)
