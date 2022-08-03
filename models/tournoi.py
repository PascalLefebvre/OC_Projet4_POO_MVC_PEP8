"""Définit un tournoi d'échecs avec ses joueurs et ses tours"""

from .donnees import NOMBRE_TOURS


class Tournoi:
    """Classe Tournoi"""

    def __init__(self, nom, lieu, description, date_debut, date_fin, controle_temps,
                 nombre_tours=NOMBRE_TOURS, statut='Ouvert'):
        self.nom = nom
        self.lieu = lieu
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.nombre_tours = nombre_tours
        self.controle_temps = controle_temps
        self.description = description
        self.statut = statut
        self.joueurs = []
        self.tours = []
        self.nombre_points = []

    def ajouter_joueur(self, joueur):
        self.joueurs.append(joueur)
        self.nombre_points.append(0)

    def ajouter_tour(self, tour):
        self.tours.append(tour)

    def cumuler_points(self, joueur, score):
        index = self.joueurs.index(joueur)
        self.nombre_points[index] += score

    def changer_statut(self, statut):
        self.statut = statut

    def __str__(self):
        return f"\nLe tournoi {self.nom} se déroulera à {self.lieu} du {self.date_debut} au {self.date_fin}\
                 \nDescription : {self.description}\nContrôle du temps : {self.controle_temps}"
