"""Définit un tournoi d'échecs
   avec ses joueurs et ses tours"""


class Tournoi:
    """Classe Tournoi"""

    def __init__(self, nom, lieu, description, date_debut, date_fin = "",
                 nombre_tours = 4):
        self.nom = nom
        self.lieu = lieu
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.nombre_tours = nombre_tours
        self.description = description
        self.joueurs = []
        self.tours = []

    def ajouter_joueur(self, joueur):
        self.joueurs.append(joueur)
    
    def ajouter_tour(self, tour):
        self.tours.append(tour)
    
    def __str__(self):
        return f"\nLe tournoi {self.nom} de {self.lieu} se déroulera le {self.date_debut}"
    
