# POC OSG-GE

Ce dépôt a pour but de faire un poc sur l'osg-ge

## Arborescence des fichiers

* app/ : dossier où se situent tous les fichiers de l'application web

    * controllers/ dossier contenant les scripts python pour les routes (toutes les actions pour une route)
        * route.py : fichier contenant toutes la route psg-ge
    
    * static/ : dossier contenant les fichiers appelés (css, js, img) dans les routes ou fichier html
        * css/ : dossier contenant les différents fichiers css (design)
        * js/ : dossier contenant les différents fichiers js (affichage dynamique)
            * osg-ge.js : fichier s'occupant de l'osge coté client
    
    * template/ : dossier qui contient tous les fichiers html appelé par les routes
        * layout/ : dossier contenant la barre de navigation et le footer d'une page html (peut être vide)
        * pages/ : dossier contenant les différentes pages appelés par les routes 
        * base : fichier contenant tout le haut commun de toutes les pages html
    
    * __init__.py : fichier qui initialise l'app + configure les différents fichiers de routes

* .gitignore : on ignore certains fichiers(venv, __pycache__, etc) aux commit

* requirements.txt : fichier contenant toutes les librairies python à installer (pip install -r requirements.txt)

* run.py, run_prod.py : script qui appelle le dossier app et qui lance l'application web (run.py en local, run_prod.py en prod)

## Run projet en local

Se mettre à la racine du projet
Si vous avez docker :

```
docker-compose up 
```

Sinon
Création et activation de l'environnement virtuel (si besoin) :

Windows :
```
py -3 -m venv venv
```
```
venv\Scripts\activate
```

Linux:
```sh
python3 -m venv venv
```
```sh
. venv/bin/activate
```

Installation des librairies :
```sh
pip install -r requirements.txt
```

Création de run.py pour lancer le serveur\
Dans run.py (mettre votre "host", si c'est en local enlever "host") :
```py
from app import app

if __name__ == "__main__":
    app.run(debug=True)
```

Lancer le serveur :

En dev :
```
python3 run.py
```

## Deploiement

git push ou merge request sur la branche main du depot git

aller sur cette url : https://gitlab.gpf-tech.ign.fr/bac-a-sable-rdd/demo-osge-deploiement/-/pipelines

Run la pipeline
