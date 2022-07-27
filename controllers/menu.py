"""Definit le contrôleur des menus de l'application."""

import time

from models.donnees import NOMBRE_JOUEURS, NOM_TOURS, NOMBRE_MATCHS
from models.joueur import Joueur
from models.tournoi import Tournoi
from models.tour import Tour
from models.match import Match
from .base import Controleur

class ControleurMenu:
    """Contrôleur des menus."""

    def __init__(self, view):
        """A une vue."""
        self.view = view
        self.controleur = Controleur(self.view)

    def gerer_menu_tournoi(self):
        """Gère le menu de gestion d'un tournoi (inscription et association des joueurs et saisie des résultats)."""
        while True:
            # Sélection du tournoi à gérer
            choix_tournoi = self.controleur.choisir_tournoi_a_gerer()
            if choix_tournoi == 0:
                return
            # Décalage de "+1" entre le numéro du choix et l'indice du tournoi correspondant
            tournoi_en_cours = self.controleur.tournois[choix_tournoi-1]
            # Déclenche les actions du sous-menu de gestion d'un tournoi
            while True:
                nombre_choix = self.view.afficher_menu_tournoi(tournoi_en_cours)
                choix = self.view.saisir_choix(nombre_choix)
                if choix == None:
                    message = "Choix invalide. Merci d'entrer un chiffre entre 0 et " + str(nombre_choix-1)
                    self.view.afficher_message(message)
                elif choix == 0:
                    break    
                elif choix == 1:
                    self.controleur.inscrire_joueurs(tournoi_en_cours)
                elif choix == 2:
                    tour_en_cours = self.controleur.creer_tour(tournoi_en_cours)
                    self.controleur.appairer_joueurs(tournoi_en_cours, tour_en_cours)
                elif choix == 3:
                    self.controleur.saisir_resultats_matchs(tournoi_en_cours)

    def gerer_menu_rapports(self):
        """Gère le menu d'édition des rapports."""
        pass

    def gerer_menu_classement(self):
        """Met à jour le classement des joueurs."""
        pass

    def gerer_menu_principal(self):
        """Gère le menu principal."""
        while True:
            nombre_choix = self.view.afficher_menu_principal()
            choix = self.view.saisir_choix(nombre_choix)
            if choix == None:
                message = "Choix invalide. Merci d'entrer un chiffre entre 0 et " + str(nombre_choix-1)
                self.view.afficher_message(message)
            elif choix == 0:
                message = "\n\nEtes-vous sûr de vouloir quitter l'application (o/n) ? "
                reponse = self.view.saisir_reponse(message)
                if reponse == 'o':
                    exit()                
            elif choix == 1:
                self.controleur.creer_tournoi()
            elif choix == 2:
                self.gerer_menu_tournoi()
            elif choix == 3:
                self.gerer_menu_classement
            elif choix == 4:
                self.gerer_menu_rapports()
            elif choix == 5:
                self.controleur.sauvegarder_donnees()
            elif choix == 6:
                self.controleur.restaurer_donnees()


