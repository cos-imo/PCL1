import argparse

parser = argparse.ArgumentParser(usage='python3 source/main.py file_name [OPTIONS]', description='Compile un programme Ada')
parser.add_argument('sourcefile', type=open)

args = parser.parse_args()
