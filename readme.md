# Presentation projet
## Nom du projet
	*FermeConnecte*
## Logo
![Logo de FermeConnecte](static/img/logo.png)
## Description

FermeConnecte est une application qui permet de mettre à disposition les produits de la grande ferme de l'ESA à la population de L'INPHB.
Elle va fonctionner comme une apllication de E-commerce.

## Fonctionnalités

1. Connexion à son profile
2. Recherche par categorie 
3. Ajout ou retrait d'un produit au panier 
4. Passer une commande 
5. Contacter les fournisseurs

# Spécifications techniques

## Technologies

FrontEnd :
----------
- html
- css
- js

BackEnd:
--------
- python3 
	+ Framework : Flask
	+ Database : Deta Base
	+ Storage : Deta Drive
	
Le dévéloppement actuelle de FermeConnecte se fait avec la technologie du microframework python **flask**.
La base de données et la gestion de fichiers est gérer actuellemnt avec Deta


## Arboressence

```bash
.
│   .gitignore
│   main.py
│   readme.md
│   requirements.txt         : [dependences] Ensembles des packages à installer
│   trouvele.py              : Programme principale (Routings...)
│   _database.py             : [module] Fonctions et objets de base de données
│   _declaration.py          : [module] Base de données déclarations(temp)
│   _forms.py                : [module] Formulaires 
│   _validation.py           : [module] Validation de données
│
├───static
│   ├───css
│   │       animate.min.css      : [Framework] Animation
│   │       daisyui.css          : [Framework] Framework UI
│   │       session_error.css    : [style] 
│   │       signup.css           : [style]
│   │       tailwind.min.css     : [Framework]
│   │       trouvele_profil.css  : [style]
│   │       validation.css       : [style]
│   │
│   ├───img                      : [Image locale]
│   │       c1.png
│   │       c2.png
│   │       c3.png
│   │       default_pp.webp
│   │       logo.png              : logo
│   │       profile-default.png   : pp par defaut
│   │
│   └───js
│           jquery.min.js
│           tailwindcss.js
│           tailwindcss.min.js
│           validation.js
│           w3.js
│
├───templates
        accueil.html
        bottom_nav.html
        carousel.html
        header.html
        index.html
        login.html
        session_error.html
        signup.html
        validation.html
```

## Réalisés:
R-A-S
## A faire

L'application est à l'étape 0.

# Demos

