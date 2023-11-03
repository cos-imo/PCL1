# Modules Python

### Structure de base d'un module

### Outil de création de module

Saisir depuis Projet:

```m
./modinit.sh <nom_du_module>
```

Ou, pour créer un module sans nom:

```
./modinit.sh
```

### Structure de base d'un 

```
.
├── module
│   ├── __init__.py
│   └── modulefile.py
```

### __ init __.py

```
from .modulefile import (...)
```

### Pour importer

```from
from module import *
```
