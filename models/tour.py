"""Définit un tour (une ronde)"""


class Tour:
    """Classe Tour

       nom    = "Round1" ou "Round2" ou etc."""

    def __init__(self, nom, date_heure_debut):
        self.nom = nom
        self.date_heure_debut = date_heure_debut
        self.date_heure_fin = ''
        self.statut = 'Ouvert'
        self.paires_joueurs = []
        self.matchs = []

    def ajouter_paire_joueurs(self, paire_joueurs):
        self.paires_joueurs.append(paire_joueurs)

    def ajouter_match(self, match):
        self.matchs.append(match)

    def cloturer(self, date_heure_fin, statut):
        self.date_heure_fin = date_heure_fin
        self.statut = statut
