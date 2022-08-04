"""Definit le contrôleur des tournois."""

from models.tournoi import Tournoi


class ControleurTournoi:
    """Crée les tournois."""

    def __init__(self, vue, tournois):
        self.vue = vue
        self.tournois = tournois

    def creer_tournoi(self):
        """Crée un tournoi."""
        nom, lieu, description, date_debut, date_fin, controle_temps = self.vue.saisir_tournoi()
        self.tournois.append(Tournoi(nom, lieu, description, date_debut, date_fin, controle_temps))
        self.vue.afficher_tournoi(self.tournois[-1])
