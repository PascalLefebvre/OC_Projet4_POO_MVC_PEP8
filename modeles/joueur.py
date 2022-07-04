"""Définit un joueur qui participe à un tournoi"""

class Joueur:
    """Classe joueur"""

    def __init__(self, nom, prenom, date_naissance, sexe, classement, nombre_points = 0):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.sexe = sexe
        self.classement = classement
        self.nombre_points = nombre_points

    def cumuler_points(self, score):
        self.nombre_points += score

    def jouer_match(self):
        pass

    def afficher_classement(self):
        print(f"Le joueur {self.nom} {self.prenom} qui a un classement de {self.classement}.")

    def afficher_points(self):
        print(f"Le joueur {self.nom} {self.prenom} a {self.nombre_points} points.")

