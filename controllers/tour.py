"""Definit le contrôleur des tours."""

import time

from models.donnees import NOM_TOURS, NOMBRE_JOUEURS
from models.tour import Tour


class ControleurTour:
    """Contrôleur des tours."""

    def __init__(self, view):
        """A une vue."""
        self.view = view

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
        """Appaire les joueurs selon le système de tournoi suisse."""
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
