# Projet Compilation

![Static Badge](https://img.shields.io/badge/Télécom-Projet_scolaire-purple)
![Static Badge](https://img.shields.io/badge/Langage-Python-yellow)
![Static Badge](https://img.shields.io/badge/Arbre-GraphViz-blue)

## Sommaire

0. [Sommaire](#Sommaire)
1. [Liste des membres](#liste-des-membres)
2. [Sujet](#Sujet)
3. [Suivi du développement](#suivi-du-developpement)


## Liste des membres

### Liste des membres - Élèves

* MOREL Célestin	[@Celestin.Morel		](https://gitlab.telecomnancy.univ-lorraine.fr/Celestin.Morel)[Celestin.Morel@telecomnancy.eu](mailto:Celestin.Morel@telecomnancy.eu)
* LO El Hadji Malick	[@El-Hadji-Malick.Lo	](https://gitlab.telecomnancy.univ-lorraine.fr/El-Hadji-Malick.Lo)[El-hadji-Malick.Lo@telecomnancy.eu](mailto:El-hadji-Malick.Lo@telecomnancy.eu)
* ZHOU Alex		[@Alex.Zhou			](https://gitlab.telecomnancy.univ-lorraine.fr/Alex.Zhou)[Alex.Zhou@telecomnancy.eu](mailto:alex.zhou@telecomnancy.eu)
* UNGARO Cosimo	[@Cosimo.Ungaro		](https://gitlab.telecomnancy.univ-lorraine.fr/Cosimo.Ungaro)[Cosimo.Ungaro@telecomnancy.eu](mailto:cosimo.ungaro@telecomnancy.eu)

### Liste des membres - Encadrants

* FESTOR Olivier	[@Olivier.festor			](https://gitlab.telecomnancy.univ-lorraine.fr/Olivier.Festor)[Olivier.Festor@telecomnancy.eu](mailto:Olivier.Festor@telecomnancy.eu)
* COLLIN Suzanne	[@Suzanne.Collin		](https://gitlab.telecomnancy.univ-lorraine.fr/Suzanne.Collin)[Suzanne.Collin@telecomnancy.eu](mailto:Olivier.Festor@telecomnancy.eu)
* BUCHI Baptiste	[@Baptiste.Buchi		](https://gitlab.telecomnancy.univ-lorraine.fr/baptiste.buchi)[Baptiste.Buchi@telecomnancy.eu](Baptiste.Buchi@telecomnancy.eu)


## Sujet

Extrait du [sujet](./documents/Sujet.pdf) 2023-2024:

> La partie PCL1 (octobre à mi-janvier) s'adressera à tous les élèves: il s'agit d'écrire les analyseurs lexicaux et syntaxiques, et d'implémenter la construction de l'arbre abstrait

## Suivi du développement
Afin de permettre à chacun de suivre l'avancement du projet et de ne pas se retrouver perdu devant les modifications effectuées par d'autres membres, le document [Suivi du développement](NULL) recoupe les denières modifications en dates et contient certains principes de développement associées au projet.

## Déploiement et structure
Afin de permettre la distribution du code, l'application python est exportée sur `pip`. La page relative au projet est disponible [ici](https://pypi.org/project/Compilateur-canAda-Zhou-Lo-Morel-Ungaro/) et peut donc être téléchargée avec
```
pip install Compilateur-canAda-Zhou-Lo-Morel-Ungaro
```


##La structure globale du projet
```bash
├── documents
│   ├── Cahier des charges
│   │   ├── biblio.bib
│   │   ├── LICENSE
│   │   ├── main.tex
│   │   ├── Projet Compilation - Cahier des charges.pdf
│   │   └── README.md
│   ├── codage_des_lexiques.txt
│   ├── doc
│   │   ├── module.md
│   │   ├── PatchNotes.md
│   │   └── Structure.md
│   ├── doc.md
│   ├── Outils de gestion de projet
│   │   └── Gantt.xlsx
│   └── Supports pédagogiques
│       ├── Ada A Crash Course.pdf
│       ├── Documentation ARM.pdf
│       ├── Langage Ada LIRMM.pdf
│       └── Sujet.pdf
├── README.md
└── source
    ├── Banque_de_tests
    │   ├── exemple_ada_.txt
    │   ├── Grammaire
    │   │   └── testRegle.py
    │   ├── Programme1.txt
    │   ├── Programme2.txt
    │   ├── Programme3.txt
    │   └── Programme4.txt
    ├── grammaire
    │   └── __pycache__
    │       ├── Grammaire.cpython-310.pyc
    │       ├── Regle.cpython-310.pyc
    │       └── RegleManager.cpython-310.pyc
    ├── main.py
    ├── modules
    │   ├── analyse_lexicale
    │   │   ├── error_handler
    │   │   │   ├── errorhandler.py
    │   │   │   └── __init__.py
    │   │   ├── token_analyser
    │   │   │   ├── __init__.py
    │   │   │   └── token_analyser.py
    │   │   └── token_generator
    │   │       ├── __init__.py
    │   │       └── token_generator.py
    │   ├── arbre
    │   │   └── arbre.py
    │   ├── arguments
    │   │   ├── arguments.py
    │   │   └── __init__.py
    │   ├── automate
    │   │   ├── automate.py
    │   │   ├── fichier_reconstruit.txt
    │   │   └── __init__.py
    │   ├── export
    │   │   ├── data_exporter.py
    │   │   └── __init__.py
    │   ├── grammaire
    │   │   ├── arbretest.py
    │   │   ├── Grammaire.py
    │   │   ├── output
    │   │   │   ├── arbre_abstrait.gv
    │   │   │   └── arbre_abstrait.gv.pdf
    │   │   ├── __pycache__
    │   │   │   ├── Grammaire.cpython-310.pyc
    │   │   │   ├── Regle.cpython-310.pyc
    │   │   │   └── RegleManager.cpython-310.pyc
    │   │   ├── RegleManager.py
    │   │   ├── Regle.py
    │   │   ├── rules.gramm
    │   │   └── words.gramm
    │   └── test_graph
    │       ├── gr.py
    │       ├── hello.gv
    │       └── hello.gv.pdf
    ├── output
    │   └── fichier_reconstruit.txt
    ├── setup.py
    └── tests
        ├── exemple_ada_2.txt
        ├── exemple_ada_.txt
        └── testLexer.py
```
ATTENTION il s'agit ici d'une version non mise à jour du code (obsolète)
