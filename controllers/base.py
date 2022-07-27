"""Definit le contrôleur principal."""

import time
from random import randint
from tinydb import TinyDB

from models.donnees import NOMBRE_JOUEURS, NOM_TOURS, NOMBRE_MATCHS, NOM_FICHIER_STOCKAGE, joueurs
from models.joueur import Joueur
from models.tournoi import Tournoi
from models.tour import Tour
from models.match import Match
from utils.storage import StoragePickle
# from .menu import ControleurMenu

class Controleur:
    """Contrôleur principal."""

    def __init__(self, view):
        """A une vue."""
        self.view = view
        self.tournois = []
        self.joueurs = []

    def initialiser_liste_joueurs(self):
        """Initialise la liste des joueurs ayant déjà participé à un tournoi"""
        for i in range(len(joueurs)):
            nom = joueurs[i][0]
            prenom = joueurs[i][1]
            date_naissance = joueurs[i][2]
            sexe = joueurs[i][3]
            classement = joueurs[i][4]
            self.joueurs.append(Joueur(nom, prenom, date_naissance, sexe, classement))

    def creer_tournoi(self):
        """Crée un tournoi."""
        nom, lieu, description, date_debut, controle_temps = self.view.saisir_tournoi()
        self.tournois.append(Tournoi(nom, lieu, description, date_debut, controle_temps))
        self.view.afficher_tournoi(self.tournois[-1])
    
    def choisir_tournoi_a_gerer(self):
        """Choisit le tournoi à gérer"""
        self.view.afficher_liste_tournois(self.tournois)
        nombre_choix = len(self.tournois)+1
        choix = self.view.saisir_choix(nombre_choix)
        if choix == None:
            message = "Choix invalide. Merci d'entrer un chiffre entre 0 et " + str(nombre_choix-1)
            self.view.afficher_message(message)
        else:
            return choix

    def inscrire_joueurs(self, tournoi):
        """Crée quelques joueurs."""
        while len(tournoi.joueurs) < NOMBRE_JOUEURS:
            nom, prenom, date_naissance, sexe, classement = self.view.saisir_joueur(len(tournoi.joueurs))
            if not nom:
                return
            joueur = Joueur(nom, prenom, date_naissance, sexe, classement)
            tournoi.ajouter_joueur(joueur)
        self.view.afficher_classement_joueurs(tournoi.joueurs)

    def choisir_tour(self):
        """Choisit le tour à gérer"""
        self.view.afficher_liste_tours()
        nombre_choix = len(NOM_TOURS)+1
        choix = self.view.saisir_choix(nombre_choix)
        if choix == None:
            message = "Choix invalide. Merci d'entrer un chiffre entre 0 et " + str(nombre_choix-1)
            self.view.afficher_message(message)
        else:
            return choix

    def creer_tour(self, tournoi):
        """Crée un tour."""
        choix = self.choisir_tour()
        if choix == 0:
            return
        else:
            tour = Tour(NOM_TOURS[choix-1], time.asctime())
            tournoi.ajouter_tour(tour)
        return tour

    def appairer_joueurs(self, tournoi, tour):
        """Appaire les joueurs."""
        nombre_paires_joueurs = int(len(tournoi.joueurs)/2)
        joueurs_ordonnes = []

        if tour.nom == NOM_TOURS[0]:
            # selon leur classement pour le premier tour
            joueurs_ordonnes = sorted(tournoi.joueurs, key=lambda joueur: joueur.classement, reverse=True)
            message = "---> Les joueurs du " + tour.nom + " sont appairés selon leur classement :\n"
            self.view.afficher_message(message)
            for i in range(nombre_paires_joueurs):
                tour.ajouter_paire_joueurs((joueurs_ordonnes[i], joueurs_ordonnes[i+nombre_paires_joueurs]))
            self.view.afficher_classement_joueurs(joueurs_ordonnes)
        else:
            # selon leurs points acquis pendant le tournoi pour les autres tours
            nombre_points = tournoi.nombre_points.copy()
            for i in range(NOMBRE_JOUEURS):
                maximum_points = 0
                for indice in range(len(nombre_points)):
                    if nombre_points[indice] > maximum_points:
                        maximum_points = nombre_points[indice]
                        indice_maximum = indice
                joueurs_ordonnes.append(tournoi.joueurs[indice_maximum])
                nombre_points[indice_maximum] = -1
            message = "---> Les joueurs du " + tour.nom + " sont appairés selon leur nombre de points :\n"
            self.view.afficher_message(message)
            for i in range(0, len(tournoi.joueurs)-1, 2):
                tour.ajouter_paire_joueurs((joueurs_ordonnes[i], joueurs_ordonnes[i+1]))
            self.view.afficher_points_joueurs(joueurs_ordonnes, tournoi)      
        
        for i in range(nombre_paires_joueurs):    
            message = tour.paires_joueurs[i][0].nom + " joue contre " + tour.paires_joueurs[i][1].nom
            self.view.afficher_message(message)
        message = "\nTaper ENTREE pour continuer ..."
        self.view.saisir_reponse(message)

    def generer_resultat_match(self, match):
        """Génère un résultat aléatoire du match"""
        nombre_aleatoire = randint(1,99)
        if nombre_aleatoire <= 33:
            match.joueur_score_1 = 1
            match.joueur_score_2 = 0
        elif nombre_aleatoire > 66:
            match.joueur_score_1 = 0
            match.joueur_score_2 = 1
        else:
            match.joueur_score_1 = 0.5
            match.joueur_score_2 = 0.5

    def jouer_matchs(self, tour, paires_joueurs):
        """Crée tous les matchs d'un tour"""
        for paires in paires_joueurs:
            for i in range(NOMBRE_MATCHS):
                match = Match(paires[0], paires[1])
                self.generer_resultat_match(match)
                tour.ajouter_match(match)
        message = "Les scores des matchs du " + tour.nom + " sont les suivants :\n"
        self.view.afficher_message(message)
        for match in tour.matchs:
            message = match.joueur_1.nom + " contre " + match.joueur_2.nom + " : " + str(match.joueur_score_1) + " à " + str(match.joueur_score_2)
            self.view.afficher_message(message)

    def calculer_points(self, tournoi, matchs):
        """Calcule les points accumulés par les joueurs lors d'un tour"""
        for match in matchs:
            tournoi.cumuler_points(match.joueur_1, match.joueur_score_1)
            tournoi.cumuler_points(match.joueur_2, match.joueur_score_2)

    def saisir_resultats_matchs(self, tournoi):
        choix = self.choisir_tour()
        tour = tournoi.tours[choix-1]
        self.jouer_matchs(tour, tour.paires_joueurs)
        self.calculer_points(tournoi, tour.matchs)
        tour.ajouter_date_heure_fin(time.asctime())
        self.view.afficher_points(tournoi, tour)

    def sauvegarder_donnees(self):
        """Problème du 'None' lors du print du classement des joueurs par exemple"""
           
        """Sauvegarde les joueurs et les tournois."""
        self.initialiser_liste_joueurs()
        with TinyDB(NOM_FICHIER_STOCKAGE, storage=StoragePickle) as db:
            db.truncate()
            db.storage.write(self.joueurs)
            db.storage.write(self.tournois)
            message = "Sauvegarde effectuée"
            self.view.afficher_message(message)
            input("Continuer ...")
            """table_joueurs = db.table('joueurs')
            table_joueurs.truncate()
            table_joueurs.storage.write(self.joueurs)
            table_tournois = db.table('tournois')
            table_tournois.truncate()
            table_tournois.storage.write(self.tournois)
            message = "Sauvegarde effectuée"
            self.view.afficher_message(message)
            input("Continuer ...")"""

    def restaurer_donnees(self):
        """Restaure les joueurs et les tournois"""

        with TinyDB(NOM_FICHIER_STOCKAGE, storage=StoragePickle) as db:
            db.storage.read()
            input("Continuer ...")
            """# table_joueurs.storage.read()
            table_joueurs.all()
            input("Continuer ...")
            # table_tournois.storage.read()
            table_tournois.all()
            input("Continuer ...")"""
