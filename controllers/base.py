"""Definit le contrôleur principal."""

import time

from models.donnees import NOMBRE_JOUEURS, NOM_TOURS, NOMBRE_MATCHS
from models.joueur import Joueur
from models.tournoi import Tournoi
from models.tour import Tour
from models.match import Match


class Controller:
    """Contrôleur principal."""

    def __init__(self, view):
        """A une vue."""
        self.view = view
    
    def creer_tournoi(self):
        """Crée un tournoi."""
        infos_tournoi = self.view.saisir_tournoi(0)
        nom = infos_tournoi[0]
        lieu = infos_tournoi[1]
        description = infos_tournoi[2]
        date_debut = infos_tournoi[3]
        tournoi = Tournoi(nom, lieu, description, date_debut)
        return tournoi

    def inscrire_joueurs(self, tournoi):
        """Crée quelques joueurs."""
        while len(tournoi.joueurs) <= NOMBRE_JOUEURS:
            infos_joueur = self.view.saisir_joueur(len(tournoi.joueurs))
            if not infos_joueur:
                return
            nom = infos_joueur[0]
            prenom = infos_joueur[1]
            date_naissance = infos_joueur[2]
            sexe = infos_joueur[3]
            classement = infos_joueur[4]
            joueur = Joueur(nom, prenom, date_naissance, sexe, classement)
            tournoi.ajouter_joueur(joueur)

    def creer_tour(self, tournoi, nom_tour):
        """Crée un tour."""
        tour = Tour(nom_tour, time.asctime())
        tournoi.ajouter_tour(tour)
        return tour

    def jouer_matchs(self, tour, paires_joueurs):
        """Crée tous les matchs d'un tour"""
        matchs = {}
        for paires in paires_joueurs:
            for i in range(NOMBRE_MATCHS):
                match = Match(paires[0], paires[1])
                resultats = match.jouer_match()
                matchs[match] = resultats
        print(f"\nLes scores des matchs du {tour.nom} sont les suivants :\n")
        for cle, valeur in matchs.items():
            print(f"{cle.joueur_1.nom} contre {cle.joueur_2.nom} : {valeur}")
        return matchs

    def calculer_points(self, matchs):
        for cle, valeur in matchs.items():
            cle.joueur_1.cumuler_points(valeur[0])
            cle.joueur_2.cumuler_points(valeur[1])

    def afficher_points(self, tour, joueurs):
        print(f"\nBilan des points des joueurs à l'issue du {tour.nom} :\n")
        for joueur in joueurs:
            joueur.afficher_points()

    def lancer(self):
        """Lance le tournoi."""
        tournoi = self.creer_tournoi()
        print(tournoi)
        self.inscrire_joueurs(tournoi)
        for i in range (len(NOM_TOURS)):
            tour = self.creer_tour(tournoi, NOM_TOURS[i])
            joueurs_ordonnes, paires_joueurs = tour.appairer_joueurs(tournoi.joueurs)
            tour.afficher_joueurs(joueurs_ordonnes)
            matchs_tour = self.jouer_matchs(tour, paires_joueurs)
            self.calculer_points(matchs_tour)
            self.afficher_points(tour, joueurs_ordonnes)
