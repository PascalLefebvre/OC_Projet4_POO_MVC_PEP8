"""Définit la vue pour l'affichage des rapports."""

from os import system
from models.donnees import NOMBRE_MATCHS

class VueRapports:
    """Vue des rapports."""

    def afficher_liste_joueurs(self, joueurs, critere_tri):
        """Affiche la liste des joueurs par ordre alphabétique ou par classement."""
        # system('clear')
        if critere_tri == "ordre alphabetique":
            joueurs_ordonnes = sorted(joueurs, key=lambda joueur: joueur.nom)
        elif critere_tri == 'classement':
            joueurs_ordonnes = sorted(joueurs, key=lambda joueur: joueur.classement, reverse=True)
        print(f"\n<--- LISTE DES JOUEURS par {critere_tri} --->\n")
        for joueur in joueurs_ordonnes:
            print(joueur)
        input("\nAppuyer sur ENTREE pour continuer ...")
        return joueurs_ordonnes

    def afficher_liste_tournois(self, tournois):
        """Affiche la liste de tous les tournois."""
        system('clear')
        print("\n<--- LISTE DES TOURNOIS --->\n")
        for i in range(len(tournois)):
            print(f"\n{i+1} -- {tournois[i].nom} de {tournois[i].lieu} ({tournois[i].statut})")
            print(f"     du {tournois[i].date_debut} au {tournois[i].date_fin} ")
        input("\nAppuyer sur ENTREE pour continuer ...")
    
    def afficher_liste_tours(self, tournoi):
        """Affiche la liste des tours."""
        print(f"\n---> Liste des tours pour le tournoi {tournoi.nom} de {tournoi.lieu} :\n")
        for i in range(len(tournoi.tours)):
            print(tournoi.tours[i].nom)
        input("\nAppuyer sur ENTREE pour continuer ...")

    def afficher_liste_matchs(self, tournoi):
        """Affiche la liste de tous les matchs d'un tournoi."""
        print(f"\n---> Liste des matchs du tournoi {tournoi.nom} de {tournoi.lieu} :")
        for i in range(len(tournoi.tours)):
            print(f"\n\n> du tour {tournoi.tours[i].nom} :\n")
            for j in range(len(tournoi.tours[i].matchs)):
                print(tournoi.tours[i].matchs[j])
        input("\nAppuyer sur ENTREE pour continuer ...")
