"""Définit un tournoi d'échecs
   avec ses joueurs et ses tours"""
"""Définit un tournoi"""

class Tournoi:
    """Classe Tournoi"""

    joueurs = []
    tours = []

    def __init__(self, nom, lieu, date_debut, date_fin = "", \
                 nombre_tours = 4, description = ""):
        self.nom = nom
        self.lieu = lieu
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.nombre_tours = nombre_tours
        self.description = description

    def inscrire_joueur(self, joueur):
        self.joueurs.append(joueur)
    
    def ajouter_tour(self, tour):
        self.tours.append(tour)
    
    def __str__(self):
        return f"\nLe tournoi {self.nom} de {self.lieu} se déroulera le {self.date_debut}"
    
