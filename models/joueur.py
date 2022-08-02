"""Définit un joueur qui participe à un tournoi"""

class Joueur:
    """Classe joueur"""

    def __init__(self, nom, prenom, date_naissance, sexe, classement):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.sexe = sexe
        self.classement = classement
    
    def modifier_classement(self, classement):
        self.classement = classement

    def __str__(self):
        return f"\nLe joueur {self.nom} {self.prenom} a un classement de {self.classement}."
