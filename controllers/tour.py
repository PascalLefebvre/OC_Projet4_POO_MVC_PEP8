"""Definit le contrôleur des tours."""

import time

from models.donnees import NOM_TOURS, NOMBRE_JOUEURS
from models.tour import Tour


class ControleurTour:
    """Contrôleur des tours."""

    def __init__(self, vue, vue_rapports):
        """A deux vues : une pour la gestion des menus et une pour celle des rapports."""
        self.vue = vue
        self.vue_rapports = vue_rapports

    def choisir_tour(self, tournoi, choix_menu_tournoi):
        """Choisit le tour à gérer"""
        premier_choix_menu = self.vue.afficher_menu_choix_tour(tournoi, choix_menu_tournoi)
        nombre_choix = len(NOM_TOURS)+1
        choix = self.vue.saisir_choix(premier_choix_menu, nombre_choix)
        if choix is None:
            message = "Choix invalide. Merci d'entrer un chiffre entre " + str(premier_choix_menu) \
                      + " et " + str(nombre_choix-1)
            self.vue.saisir_reponse(message)
        return choix

    def creer_tour(self, tournoi, choix):
        """Crée un tour."""
        tour = Tour(NOM_TOURS[choix - 1], time.asctime())
        tournoi.ajouter_tour(tour)
        return tour

    def appairer_joueurs(self, tournoi, tour):
        """Appaire les joueurs selon le système de tournoi suisse."""
        nombre_paires_joueurs = int(len(tournoi.joueurs)/2)
        joueurs_ordonnes = []

        if tour.nom == NOM_TOURS[0]:
            # Appaire selon le classement pour le premier tour.
            joueurs_ordonnes = self.vue_rapports.afficher_liste_joueurs(tournoi.joueurs, 'classement')
            message = "---> Les joueurs du " + tour.nom + " sont appairés selon leur classement :\n"
            self.vue.afficher_message(message)
            for i in range(nombre_paires_joueurs):
                tour.ajouter_paire_joueurs((joueurs_ordonnes[i], joueurs_ordonnes[i+nombre_paires_joueurs]))

        else:
            # Appaire selon les points acquis pendant le tournoi pour les autres tours.
            nombre_points = tournoi.nombre_points.copy()
            # Crée une liste ordonnée de joueurs, de celui ayant le plus de points à celui en ayant le moins.
            for i in range(NOMBRE_JOUEURS):
                maximum_points = 0
                for indice in range(len(nombre_points)):
                    if nombre_points[indice] > maximum_points:
                        maximum_points = nombre_points[indice]
                        indice_maximum = indice
                joueurs_ordonnes.append(tournoi.joueurs[indice_maximum])
                nombre_points[indice_maximum] = -1

            self.vue.afficher_points_joueurs(tournoi, joueurs_ordonnes)
            message = "---> Les joueurs du " + tour.nom + " sont appairés selon leur nombre de points :\n"
            self.vue.afficher_message(message)
            for i in range(0, len(tournoi.joueurs)-1, 2):
                tour.ajouter_paire_joueurs((joueurs_ordonnes[i], joueurs_ordonnes[i+1]))

        # Affiche les matchs.
        for i in range(nombre_paires_joueurs):
            message = tour.paires_joueurs[i][0].nom + " joue contre " + tour.paires_joueurs[i][1].nom
            self.vue.afficher_message(message)
        message = "\nTaper ENTREE pour continuer ..."
        self.vue.saisir_reponse(message)
