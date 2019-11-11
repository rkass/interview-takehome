from setuptools import find_packages, setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

version = 1.0

setup(
    name='searcher',
    version=version,
    python_requires='>=3.7.4',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'load-data=searcher.data_loader:load_data'
        ]
    },
    install_requires=requirements
)