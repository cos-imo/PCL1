from setuptools import setup, find_packages 

setup(
        name='Compilateur-canAda-Zhou-Lo-Morel-Ungaro-test',
        version='0.1',
        description='Compilateur canAda',
        packages=find_packages(),
        entry_points={
            'console_scripts': [
                'ca = main:main',
            ],
        },
        )
