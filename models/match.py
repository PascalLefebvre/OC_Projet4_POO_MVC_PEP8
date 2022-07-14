"""Définit un match entre deux joueurs"""

from random import randint


class Match:
    """Classe Match"""

    joueur_1 = None
    joueur_2 = None
    joueur_score_1 = None
    joueur_score_2 = None

    def __init__(self, joueur1, joueur2):
        self.joueur_1 = joueur1
        self.joueur_2 = joueur2
    
    def jouer_match(self):
        """Renvoi un résultat aléatoire du match"""
        nombre_aleatoire = randint(1,99)
        if nombre_aleatoire <= 33:
            self.joueur_score_1 = 1
            self.joueur_score_2 = 0
        elif nombre_aleatoire > 66:
            self.joueur_score_1 = 0
            self.joueur_score_2 = 1
        else:
            self.joueur_score_1 = 0.5
            self.joueur_score_2 = 0.5

    def __str__(self):
        return f"\n{self.joueur_1.nom} joue contre {self.joueur_2.nom}"