"""Vue principale"""

from models.donnees import joueurs, tournois


class Vue:
    """Vue du tournoi d'échecs."""

    def saisir_tournoi(self, index):
        """Saisie les données d'un tournoi."""
        print(f"\nSaisie les données d'un tournoi.")
        try:
            infos_tournoi = tournois[index]
        except IndexError:
            return None
        return infos_tournoi

    def saisir_joueur(self, index):
        """Saisie les données d'un joueur."""
        print(f"\nSaisie les données d'un joueur.")
        try:
            infos_joueur = joueurs[index]
        except IndexError:
            return None
        return infos_joueur

