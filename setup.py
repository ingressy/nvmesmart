from setuptools import setup, find_packages

setup(
    name="nvmesmart",             # Name des Pakets
    version="0.1.3",                     # Versionsnummer
    description="a easy cli and maybe gui smart tool for linux",  # Kurzbeschreibung
    author="ingressy",
    license="MIT",                       # Lizenz
    packages=find_packages(),# Findet automatisch alle Python-Pakete
    py_modules=["main"],
    entry_points={
        "console_scripts": [
            "nvmesmart=main:main",  # Befehl -> Funktion
        ]
    },
    install_requires=[],                 # Abhängigkeiten (requirements.txt)
    python_requires=">=3.6",             # Minimale Python-Version
)
