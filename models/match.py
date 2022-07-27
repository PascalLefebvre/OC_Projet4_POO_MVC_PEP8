"""Définit un match entre deux joueurs"""

class Match:
    """Classe Match"""

    joueur_1 = None
    joueur_2 = None
    joueur_score_1 = None
    joueur_score_2 = None

    def __init__(self, joueur1, joueur2):
        self.joueur_1 = joueur1
        self.joueur_2 = joueur2
    
    def __str__(self):
        return f"\n{self.joueur_1.nom} joue contre {self.joueur_2.nom}"