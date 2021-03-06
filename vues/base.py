"""Vue principale"""

from os import system
from models.donnees import joueurs_inscrits, NOM_TOURS

class Vue:
    """Vue du tournoi d'échecs."""

    def saisir_choix(self, nombre_choix):
        try:
            choix = int(input("\nEntrez votre choix : "))
        except ValueError:
            return None
        if choix in range(0, nombre_choix):
            return choix
        else:
            return None

    def afficher_menu_principal(self):
        """Affiche le menu principal."""
        menu_principal = {
            1: "Créer un nouveau tournoi",
            2: "Gérer un tournoi",
            3: "Mettre à jour le classement",
            4: "Editer les rapports",
            5: "Sauvegarder les données",
            6: "Restaurer les données",
            0: "Quitter"
            }
        system('clear')
        print("\n<--- APPLICATION TOURNOIS D'ECHECS --->\n")
        for cle in menu_principal.keys():
            print('\n', cle, '--', menu_principal[cle])
        return len(menu_principal.keys())
    
    def afficher_tournoi(self, tournoi):
        """Affiche les donnees d'un tournoi"""
        print(tournoi)
        input("\nTaper ENTREE pour continuer ...")
    
    def afficher_liste_tournois(self, tournois):
        """Affiche la liste des tournois."""
        print("\n<--- Choisissez le tournoi à gérer dans la liste ci-dessous :\n")
        for i in range(len(tournois)):
            print(f"{i+1} -- {tournois[i].nom}")
        print(f"0 -- Revenir au menu principal")

    def saisir_tournoi(self):
        """Saisie les données d'un tournoi."""
        system('clear')
        print("\n<--- CREATION D'UN TOURNOI --->\n\nEntrez :")
        name = input("\nle nom : ")
        lieu = input("\nle lieu : ")
        date_debut = input("\nla date de début : ")
        controle_temps = input("\nle contrôle du temps (bullet, blitz ou coup rapide) : ")
        description = input("\nun commentaire : ")
        return (name, lieu, description, date_debut, controle_temps)
    
    def afficher_menu_tournoi(self, tournoi):
        """Affiche le menu de gestion d'un tournoi."""
        menu_tournoi = {
            1: "Inscrire les joueurs à un tournoi",
            2: "Générer les paires de joueurs pour un tour",
            3: "Saisir les résultats des matchs d'un tour",
            0: "Revenir au menu principal"
            }
        system('clear')
        print(f"<--- GESTION DU TOURNOI D'ECHEC {tournoi.nom} --->")
        for cle in menu_tournoi.keys():
            print('\n', cle, '--', menu_tournoi[cle])
        return len(menu_tournoi.keys())

    def saisir_joueur(self, index):
        """Saisie les données d'un joueur."""
        try:
            infos_joueur = joueurs_inscrits[index]
        except IndexError:
            return None
        return infos_joueur
    
    def afficher_classement_joueurs(self, joueurs):
        """Affiche le classement des joueurs du tournoi."""
        for joueur in joueurs:
            joueur.afficher_classement()
        input("\nTaper ENTREE pour continuer ...")

    def afficher_points_joueurs(self, joueurs, tournoi):
        """Affiche le total des points cumulés des joueurs du tournoi."""
        for joueur in joueurs:
            indice = tournoi.joueurs.index(joueur)
            print(f"\nLe joueur {joueur.nom} {joueur.prenom} a {tournoi.nombre_points[indice]} points.")
        input("\nTaper ENTREE pour continuer ...")

    def afficher_liste_tours(self):
        """Affiche la liste des tours."""
        print("\n---> Choisissez le tour pour la génération des paires dans la liste ci-dessous :\n")
        for i in range(len(NOM_TOURS)):
            print(f"{i+1} -- {NOM_TOURS[i]}")
        print(f"0 -- Revenir au menu précédent")

    def afficher_points(self, tournoi, tour):
        print(f"\n---> Bilan des points des joueurs à l'issue du {tour.nom} :\n")
        for joueur in tournoi.joueurs:
            index = tournoi.joueurs.index(joueur)
            print(f"\nLe joueur {joueur.nom} {joueur.prenom} a {tournoi.nombre_points[index]} points.")
        input("\nTaper ENTREE pour continuer ...")
