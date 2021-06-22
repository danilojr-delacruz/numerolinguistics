from setuptools import setup, find_packages

setup(
    name='example',
    version='1.0',
    packages=find_packages(
        where="numerolinguistics"
        ),
    install_requires=[
        "networkx",
        "unidecode",
    ]
)