# Suivi du développement

## Sommaire
0. [Sommaire](sommaire)
1. [Principes de développement](principes-de-developpement)
    1.1. [Structure du projet](structure-du-projet)
2. [Patch notes](patch-notes)

## Remarque préliminaire
Ce document à été créé en cours de projet. Aisni, certains éléments devant figurer dans les Patch notes se trouvent, par facilité de rédaction, dans "Principes de développement". Ceux-ci seront au fur et à mesure déplacés vers patch notes

## Principes de dévelopemment

### Structure du projet
Afin de faciliter le code ainsi que la distribution, le code sera scindé en module. L'ensemble des modules sera importé dans le script main.py (à la base de l'arborescence) qui se chargera de l'ensemble des tâches relatives au bon fonctionnement du programme: parsing des arguments, appels au modules etc...
L'objectif étant de créer un compilateur, le code aura donc la structure suivante:
``` 
.
├── analyse_lexicale
│   ├── token_analyser
│   │   ├── __init__.py
│   │   └── token_analyser.py
│   └── token_generator
│       ├── __init__.py
│       └── token_generator.py
├── arguments
│   ├── __init__.py
│   └── arguments.py
├── export
│   ├── __init__.py
│   ├── data_exporter.py
├── main.py
├── setup.py
└── tests
    └── (fichiers de test)
```

Le dossier analyse_lexicale comprend les modules nécessaires à l'analyse lexicale: génération de token ...
Le dossier arguments comprend le parser (implémenté sur argsparse)
export comprend les script liés à l'exportation de données intermédiaires (création de dump files)
setup.py est un setup script classique permettant d'exporter l'application sur PyPi ou TestPyPi.
Enfin, tests comprend l'ensemble des scripts dédiés aux tests de l'application.

### Constitution des modules
Afin de faciliter la lecture du code ainsi que la création de tests, les modules seront (à quelques exceptions prêt) constitué d'un fichier __init__.py permettant d'initialiser le module, ainsi que d'un ou plusieurs scripts principaux contenant le code, lui-même organisé sous forme de classe(s).

### Bons principes de développement
Afin de permettre ) tout un chacun de s'y retrouver, il est demandé aux développeurs, dès lors qu'ils implémentent une fonction:

0. Bien entendu, de respecter l'organisation du projet énoncée ci-dessus
1. D'écrire un commit clair, permettant de comprendre précisemment les modifications apportées, et qui ne comporte qu'un seul changement.
2. De penser à venir écrire une patch note si la modification en vaut la peine
3. D'ajouter une option au parser ainsi que le message d'aide correspondant qui permettra aux utilisateurs de comprendre précisemment la fonction ainsi implémenté, son utilité ainsi que son utilisation

Il est à noter que le message d'aide du parser constitue une base d'informations primordiale, il convint donc d'écrire les messages d'aides correspondant le plus tôt possible
