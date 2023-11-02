import pickle, sys, os
from pathlib import Path

dictionnary={}

def write():
    with open('input', 'wb') as f:
        pickle.dump(dictionnary, f)

def load():        
    with open('input', 'rb') as f:
        read_dictionnary = pickle.load(f)
    return read_dictionnary

def main():
    global dictionnary
    if os.path.isfile('input'):
        load()
        dictionnary=load()
    else:
        Path(str(os.getcwd())+"/input").touch()
        dictionnary={}
    while 1:
        entree=input("$ ")
        if entree==("quit") or entree==("exit"):
            write()
            exit()
        elif entree.split(" ")[0]=="add":
            key, value = (entree.split(" ")[1]).split(":")
            dictionnary[key]=value
        elif entree=="show":
            print(dictionnary)
        else:
            sys.stdout.write("Erreur \nCommande non reconnue \n\nUtilisation: \t$ [clé]:[valeur]\n\t\tshow\n\t\tquit\n\n")

if __name__=="__main__":
    main()