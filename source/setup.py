from setuptools import setup, find_packages 

setup(
        name='ca',
        version='0.1',
        description='Compilateur canAda',
        packages=['.','token_analyser','token_generator','arguments'],
        entry_points={
            'console_scripts': [
                'ca = main:main',
            ],
        },
        )
