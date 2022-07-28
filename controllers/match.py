"""Definit le contrôleur des matchs d'échecs."""

import time
from random import randint

from models.donnees import NOMBRE_MATCHS
from models.match import Match


class ControleurMatch:
    """Contrôleur des matchs."""

    def __init__(self, view):
        """A une vue."""
        self.view = view

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
            message = match.joueur_1.nom + " contre " + match.joueur_2.nom + " : " \
                      + str(match.joueur_score_1) + " à " + str(match.joueur_score_2)
            self.view.afficher_message(message)

    def calculer_points(self, tournoi, matchs):
        """Calcule les points accumulés par les joueurs lors d'un tour"""
        for match in matchs:
            tournoi.cumuler_points(match.joueur_1, match.joueur_score_1)
            tournoi.cumuler_points(match.joueur_2, match.joueur_score_2)

    def saisir_resultats_matchs(self, tournoi, choix):
        tour = tournoi.tours[choix-1]
        self.jouer_matchs(tour, tour.paires_joueurs)
        self.calculer_points(tournoi, tour.matchs)
        tour.ajouter_date_heure_fin(time.asctime())
        self.view.afficher_points(tournoi, tour)
