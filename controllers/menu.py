"""Definit le contrôleur des menus de l'application."""

import time

from models.donnees import NOMBRE_JOUEURS, NOM_TOURS, NOMBRE_MATCHS
from models.joueur import Joueur
from models.tournoi import Tournoi
from models.tour import Tour
from models.match import Match
from .base import Controller


class Menu:
    """Contrôleur des menus."""

    def __init__(self, view):
        """A une vue."""
        self.view = view

    def gerer_menu_principal(self):
        """Déclenche les actions du menu principal en fonction du choix de l'utilisateur"""
        while (True):
            self.view.afficher_menu_principal()
            choix = ''
            try:
                choix = int(input("Entrez votre choix : "))
            except ValueError:
                print("Merci d'entrer un chiffre ...")
            if choix == 1:
                pass

