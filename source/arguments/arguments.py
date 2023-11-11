import argparse

class Parser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(usage='python3 source/main.py file_name [OPTIONS]', add_help=False, description='Compile un programme Ada')
        self.parser.add_argument('sourcefile', type=open)

        self.parser.add_argument('-h','--help', action='help', help="Affiche ce message d'aide")
        self.parser.add_argument('-v','--verbose', action="store_true", help="Active le mode verbose (tout s'affiche)")

        self.args = self.parser.parse_args()

