import argparse

class Parser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(usage='python3 source/main.py file_name [OPTIONS]', add_help=False, description='Compile un programme Ada')
        self.parse_arguments()

    def parse_verbose_mode(self, option):
        abb={"mode-1":"1", "mode-2":"2", "token-liste":"2", "mode-3":"3", "table-identificateurs":"3"}

        if option in abb:
            return abb[option]
        else:
            return option

    def parse_arguments(self):
        self.parser.add_argument('sourcefile', type=open)

        self.parser.add_argument('-h','--help', action='help', help="Affiche ce message d'aide")
        self.parser.add_argument('-v','--verbose', nargs='?', const="1", choices=["1", "2", "3"], type=self.parse_verbose_mode, help="Active le mode verbose (tout s'affiche)")
        self.parser.add_argument('-t', '--token-list', help="Affiche la liste des tokens générés (équivalent au second mode de verbose)")
        self.parser.add_argument('-i', '--table-identificateurs', help="Affiche la table des identificateurs (équivalent au troisième mode de verbose)")

        self.args = self.parser.parse_args()

