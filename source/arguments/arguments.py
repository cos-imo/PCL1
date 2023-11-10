import argparse

parser = argparse.ArgumentParser(usage='python3 source/main.py file_name [OPTIONS]', add_help=False, description='Compile un programme Ada')
parser.add_argument('sourcefile', type=open)

parser.add_argument('-h','--help', action='help', help="Affiche ce message d'aide")
parser.add_argument('-v','--verbose', action="store_true", help="Active le mode verbose (tout s'affiche)")

args = parser.parse_args()
