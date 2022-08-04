"""Definit le contrôleur des matchs d'échecs."""

import time
from random import randint

from models.donnees import NOMBRE_TOURS, NOMBRE_MATCHS
from models.match import Match


class ControleurMatch:
    """Contrôleur des matchs."""

    def __init__(self, vue):
        """A une vue pour la gestion des menus."""
        self.vue = vue

    def saisir_resultats_matchs(self, tournoi, choix):
        """Crée tous les matchs d'un tour, saisie leur résultat et cumule les points acquis."""
        tour = tournoi.tours[choix-1]
        self.jouer_matchs(tour, tour.paires_joueurs)
        self.calculer_points_joueurs(tournoi, tour.matchs)
        tour.cloturer(time.asctime(), 'Terminé')
        if len(tournoi.tours) == NOMBRE_TOURS:
            tournoi.changer_statut('Terminé')


    def jouer_matchs(self, tour, paires_joueurs):
        """Crée tous les matchs d'un tour et les joue de façon aléatoire."""
        for paires in paires_joueurs:
            for i in range(NOMBRE_MATCHS):
                match = Match(paires[0], paires[1])
                self.generer_resultat_match(match)
                tour.ajouter_match(match)
        message = "Les scores des matchs du " + tour.nom + " sont les suivants :\n"
        self.vue.afficher_message(message)
        for match in tour.matchs:
            message = match.__str__()
            self.vue.afficher_message(message)
        message = "\nAppuyer sur ENTREE pour continuer ..."
        self.vue.saisir_reponse(message)

    def generer_resultat_match(self, match):
        """Génère un résultat aléatoire du match et le stocke."""
        nombre_aleatoire = randint(1, 99)
        if nombre_aleatoire <= 33:
            match.rentrer_score(1, 0)
        elif nombre_aleatoire > 66:
            match.rentrer_score(0, 1)
        else:
            match.rentrer_score(0.5, 0.5)

    def calculer_points_joueurs(self, tournoi, matchs):
        """Cumule les points acquis par les joueurs lors d'un tour."""
        for match in matchs:
            tournoi.cumuler_points(match.joueur_1, match.joueur_score_1)
            tournoi.cumuler_points(match.joueur_2, match.joueur_score_2)
