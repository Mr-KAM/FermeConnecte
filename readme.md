# Presentation projet
## Nom du projet :
*ESA FermeConnecte*
## Logo
![Logo de trouvele](static/img/logo.png)
## Description

Application web de commande en ligne des produits de la grande ferme de l'ESA/INP-HB.

## Fonctionnalités
1. Creer un compte utilisateur
2. Connexion à son compte
3. Rechercher une produit dans le catalogue des produits disponibles
4. Ajouter un produit et la quantité souhaité à son panier
5. Planifier sa commande et le mode de paiement
6. Contacter les gestionnaires de la ferme

## Configuration de l'environnement de travail

Pour configurer votre environnement de travail, vous devez suivre les étapes suivantes:

### Clonner le repertoire de travail
Executer dans le terminal dans votre dossier de travail la commande suivante:

```bash	
git clone https://github.com/Mr-KAM/FermeConnecte.git
cd FermeConnecte
```

### Configurer l'environnment python

1- Vous devez creer un environnment virtuel. Installez **pew** via la commande:

```bash	
pip install pew
```

2- Creez un environnement virtuel 

```bash	
pew new fermeconnecte
```

3- Installez les dependences python

```bash	
pip install -r requirements.txt
```

### Lancez l'application flask

Pour executer l'application vous devez faire en ligne de commande dans le répertoire de travail:

```bash	
python app.py
```
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
	
Le dévéloppement actuelle de l'application se fait avec la technologie du microframework python **flask**.
La base de données et la gestion de fichiers est gérer actuellemnt avec Deta.


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
- Splash screen
- carousel
- signup
- validation par e-mail
- login
	+ login
	+ logout

## A faire

- validation par sms 
- validation par whatsapp
- declaration
- restauration de mot de passe
- Contacter un autre utilisateur de la communauté

# Demos

![Gif 1](demo/demo1.gif) 

![Gif 2](demo/demo2.gif) 

![Gif 3](demo/demo3.gif) 

![Gif 4](demo/demo4.gif)
