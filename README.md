# Openclassrooms - Projet 4 : Développez un programme logiciel en Python

	Pour un club d'échecs, développement d'une application de gestion des tournois
	hebdomadaires fonctionnant en mode hors ligne. Les joueurs sont appairés pour
	les matchs des différents tours selon le système de tournoi suisse.
	Le code doit suivre les directives de la PEP8 et être structuré selon le modèle
	de conception MVC (modèles, vues, contrôleurs).
	

## Installation et exécution

	$ python -m venv env
	$ source env/bin/activate
	$ pip install -r "requirements.txt"
	$ python main.py
		

## Utilisation de l'application

* Lorsque l'application est lancée pour la première fois, il n'y a aucune données.
  Pour charger une base de données minimale avec quelques joueurs et tournois (clôturés),
  commencer par l'option "Restaurer les données" du menu principal. Vous pourrez
  alors générer les différents rapports et mettre à jour le classement des joueurs
  (accessible uniquement si tous les tournois ont été clôturés).
  
  A noter que la base de données est stockée dans le fichier "db.pickle", l'outil
  Pickle étant utilisé pour la (dé)sérialisation des données.

* Après avoir créé un nouveau tournoi, vous pouvez le gérer en le sélectionnant via
  l'option "Gérer un tournoi" du menu principal.
  
  Par défaut, il a été choisi de pouvoir inscrire 8 joueurs, de dérouler le tournoi
  sur quatre tours (rounds) avec trois matchs par tour.

* L'inscription des joueurs est effectuée à partir de la base de données existante
  (pour un joueur ayant déjà participé à un tournoi) et de la saisie de nouveaux
  joueurs. Lors de la saisie du nom, si celui-ci est déjà répertorié, il est
  automatiquement inscrit, sinon, il faut saisir toutes les informations nécessaires
  à l'inscription d'un "nouveau" joueur.

* Une fois l'inscription des joueurs effectuée, la chronologie des actions est, pour
  chaque tour, de générer les paires de joueurs puis de saisir les résultats des matchs.
  
  A noter que pour faciliter le test de l'application, les résultats des matchs sont
  générés aléatoirement et saisis automatiquement !


### Génération du rapport de peluchage avec Flake8

* Depuis le répertoire de l'application, taper la commande :

  $ flake8 .

* Le rapport est accessible en ouvrant le fichier "./flake_report/index.html"

