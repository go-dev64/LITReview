# OCR_Projet_9
# LITReview

Développez une application Web en utilisant Django

## Scénario
Après un entretien réussi, vous décrochez le poste de lead développeur Python pour la jeune startup LITReview.
LITReview cherche à mettre en place une application web pour leur MVP (minimum viable product, ou produit viable minimum).
Son objectif est de commercialiser un produit, permettant à une communauté d'utilisateurs de consulter ou de solliciter une critique de livres à la demande.


<center>

![Logo de LITReview](static\images\logo_litreview.png)
# LITReview

</center>

# Projet : Application de gestion de tournoi d'échec
1. [Général / Présentation](#Général)
2. [Technologies](#technologies)
3. [Installation](#installation)
4. [Collaboration](#collaboration)
5. [Fonctionnement](#fonctionnement)
6. [License](#licence)


## <a id = Général>Général / Présentation</a>
***
Cette application Web permet aux utilisateur de demander ou publier des critiques de livres ou d’articles.

L’application présente deux cas d’utilisation principaux : 

1. Les personnes qui demandent des critiques sur un livre ou sur un article particulier.
2. Les personnes qui recherchent des articles et des livres intéressants à lire, en se basant sur les critiques des autres.

Les fonctionnalités d'inscription et de connexion sont indispensables dans le cadre de ce MVP. Lorsqu'un utilisateur se connecte au système, son flux est la première page qu'il voit. Il peut y voir les tickets et les avis de tous les utilisateurs qu'il suit. Il doit également voir ses propres tickets et avis, ainsi que tous les avis en réponse à ses propres tickets - même s'il ne suit pas l'auteur de l'avis.

Un ticket peut etre considéré comme une demande d'évaluation de la part d'un utilisateur. Il publie son billet pour demander une critique d'un livre ou d'un article de littérature. Les utilisateurs qui le suivent peuvent alors soumettre leurs critiques en réponse au billet. Les utilisateurs peuvent publier des critiques pour des livres et des articles qui n'ont pas encore fait l'objet d'un billet.

Les utilisateurs pourront suivre d'autres utilisateurs et ont également la possibilité de les désapprouver. Comme il ne s'agit que d'un MVP, cette fonctionnalité reste assez simple.

Une page répertorie tous les utilisateurs que l'utilisateur connecté suit, avec la possibilité de les désabonner.

Une page à partir de laquelle les utilisateurs pourront consulter leurs propres contributions. Ils peuvent voir leurs messages, les modifier et les supprimer à partir de cette page.


## <a id = technologies>Technologies</a>
***
L'application est developpée sous le framework Django ainsi que Boostrap 5.1.3.

Elle utilse les languages suivant:
* [Python](https://www.python.org/downloads/release/python-31012/) : Version 3.10
* HTML
* CSS
* Base de donnée : SQLite

## <a id = installation>Installation</a>
***
> **Installation** > Python doit etre instalé sur votre machine.

Toutes les opérations suivantes seront exécutées dans ce répertoire courant.

### _**Création environnement Virtuel**_

Por créer un environnement virtuel, taper dans votre terminal les commandes suivantes : 


> Sous Windows:
> ````commandline
> py -m venv env 
>````

> Sous Unix/Mac:
>````commandline
>python3 -m venv env
>````

### _**Activation environnement Virtuel**_

Pour activer ce dernier, taper les instructions suivantes toujours dans votre terminal :

> Sous Windows:
> ````commandline
> env\scripts\activate
>````

> Sous Unix/Mac:
>````commandline
>source env/bin/activate
>````

Votre terminal affichera la ligne de commande comme ci-dessous, confirmant l'activation de l'environnement virtuel :

````
(venv) PS C:\xxx\xxxx\xxxx\LITReview>
````


###  **_Installation des packages_**

Taper dans votre terminal les commandes suivantes : 

> Sous Windows:
> ````commandline
> py -m pip install -r requirements.txt
>````

> Sous Unix/Mac:
>````commandline
>python3 -m pip install -r requirements.txt
>````


Cette commande permet l'installation de tous les packages nécessaire au fonctionnement de l'application.


## <a id= fonctionnement>Fonctionnement</a>
***

###  **_Lancement de l'application_**

Le lancement de l'application s'effectue avec la commande suivante dans le terminal :

> ````commandline
> py manage.py runserver
>````

Le terminal affichera :

![Terminal](static\images\terminal.png)


Ensuite taper l'adresse suivante dans votre navigateur:

> ````commandline
> http://127.0.0.1:8000/
>````


###  **_Identifiant de connexion_**

Voici les identifiants de connexion pour les différents utilisateurs.

***_User 1_***
- pseudonyme : user_1
- mot de passe : password_user_1

***_User 2_***
- pseudonyme : user_2
- mot de passe : password_user_2

***_User 3_***
- pseudonyme : user_3
- mot de passe : password_user_3

***_User 4_***
- pseudonyme : user_4
- mot de passe : password_user_4

***_User 5_***
- pseudonyme : user_5
- mot de passe : password_user_5

***_admin_***
- pseudonyme : admin
- mot de passe : admin


***
## <a id = licence>Licence</a>


* [Licence ouverte](https://www.etalab.gouv.fr/wp-content/uploads/2017/04/ETALAB-Licence-Ouverte-v2.0.pdf) : Version 2.0
***
