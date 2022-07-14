"""Définit un tour (une ronde)"""

class Tour:
    """Classe Tour
    
       nom    = "Round1" ou "Round2" ou etc."""

    def __init__(self, nom, date_heure_debut):
        self.nom = nom
        self.date_heure_debut = date_heure_debut
        self.paires_joueurs = []
        self.matchs = []
        self.date_heure_fin = ''

    def ajouter_paire_joueurs(self, paire_joueurs):
        """Ajoute un match"""
        self.paires_joueurs.append(paire_joueurs)
    
    def ajouter_match(self, match):
        """Ajoute un match"""
        self.matchs.append(match)
    
    def ajouter_date_heure_fin(self, date_heure_fin):
        self.date_heure_fin = date_heure_fin
