"""Définit un tournoi d'échecs avec ses joueurs et ses tours"""

from .donnees import NOMBRE_TOURS

class Tournoi:
    """Classe Tournoi"""

    def __init__(self, nom, lieu, description, date_debut, controle_temps, date_fin = '', nombre_tours = NOMBRE_TOURS):
        self.nom = nom
        self.lieu = lieu
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.nombre_tours = nombre_tours
        self.controle_temps = controle_temps
        self.description = description
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
    
    def __str__(self):
        return f"\nLe tournoi {self.nom} se déroulera le {self.date_debut} à {self.lieu} \
                 \nDescription : {self.description}\nContrôle du temps : {self.controle_temps}"
    
