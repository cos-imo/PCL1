#!/bin/bash

if [ -z "$1" ]; then
    mkdir source/module_sans_nom
    echo "from .module_sans_nom_script  import main" >> source/module_sans_nom/__init__.py
    echo -e "if __name__=='__main__':\n\tmain()\n\ndef main():\n\t">>source/module_sans_nom/module_sans_nom_script.py
    echo "Module sans nom initialisé"
    exit 0
else
    module_name="$1"
    script_name=${module_name}_script.py
    dir=source/$module_name

    if [ -d "$dir" ]; then
            echo "Module '$module_name' pré-existant. Veuillez choisir un autre nom."
            exit 1
        else
            mkdir $dir
            echo "from ."$module_name"_script  import main" >> $dir/__init__.py
            echo -e "if __name__=='__main__':\n\tmain()\n\ndef main():\n\t">>$dir/$script_name
            exit 0
        fi
fi