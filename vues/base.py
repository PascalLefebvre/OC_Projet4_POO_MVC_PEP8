"""Vue principale"""

from os import system
from models.donnees import NOM_TOURS


class Vue:
    """Vue du tournoi d'échecs."""

    def afficher_menu_principal(self):
        """Affiche le menu principal."""
        menu_principal = {
            1: "Créer un nouveau tournoi",
            2: "Gérer un tournoi",
            3: "Mettre à jour le classement des joueurs",
            4: "Editer les rapports",
            5: "Sauvegarder les données",
            6: "Restaurer les données",
            0: "Quitter"
            }
        system('clear')
        print("\n<--- APPLICATION TOURNOIS D'ECHECS --->\n")
        print("         - Menu principal -\n")
        for cle in menu_principal.keys():
            print('\n', cle, '--', menu_principal[cle])
        return len(menu_principal.keys())

    def saisir_tournoi(self):
        """Saisie les données d'un tournoi pour en créer un nouveau.
           Choix '1' du menu principal."""
        system('clear')
        print("\n<--- CREATION D'UN TOURNOI --->\n\nEntrez :")
        name = input("\nle nom : ")
        lieu = input("\nle lieu : ")
        date_debut = input("\nla date de début : ")
        date_fin = input(f"\nla date de fin ({date_debut} par défaut) : ")
        if date_fin == "":
            date_fin = date_debut
        controle_temps = input("\nle contrôle du temps (bullet, blitz ou coup rapide) : ")
        description = input("\nun commentaire : ")
        return (name, lieu, description, date_debut, date_fin, controle_temps)

    def afficher_menu_choix_tournoi(self, tournois):
        """Affiche le menu du choix du tournoi à gérer.
           Choix '2' du menu principal."""
        system('clear')
        print("\n<--- CHOIX DU TOURNOI --->")
        print("\n\nChoisissez un tournoi dans la liste ci-dessous :\n")
        for i in range(len(tournois)):
            print(f"{i+1} -- {tournois[i].nom} ({tournois[i].statut})")
        print("0 -- Revenir au menu principal")

    def afficher_menu_gerer_tournoi(self, tournoi):
        """Affiche le menu de gestion d'un tournoi.
           Choix '2' du menu principal."""
        menu_tournoi = {
            1: "Inscrire les joueurs à un tournoi",
            2: "Générer les paires de joueurs pour un tour",
            3: "Saisir les résultats des matchs d'un tour",
            0: "Revenir au menu précédent"
            }
        system('clear')
        print(f"<--- GESTION DU TOURNOI D'ECHEC {tournoi.nom} de {tournoi.lieu} --->")
        for cle in menu_tournoi.keys():
            print('\n', cle, '--', menu_tournoi[cle])
        return len(menu_tournoi.keys())

    def saisir_joueur(self):
        """Saisie les données d'un joueur s'il n'est pas répertorié.
           Choix '1' du menu principal."""
        print("\nEntrez :")
        prenom = input("\nle prénom : ")
        date_naissance = input("\nla date de naissance : ")
        sexe = input("\nle sexe : ")
        while True:
            try:
                classement = int(input("\nle classement : "))
                break
            except ValueError:
                message = "Merci d'entrer un nombre. Appuyer sur ENTREE pour continuer ..."
                self.saisir_reponse(message)
                continue
        return (prenom, date_naissance, sexe, classement)

    def afficher_menu_choix_tour(self, tournoi, choix_menu):
        """Affiche le menu du choix du tour à gérer.
           Choix '2' (paires) et '3' (résultats) du menu de gestion d'un tournoi.
           Les tours qui sont clôturés ne sont pas proposés."""
        nombre_tours_ouverts = 0
        nombre_tours_termines = 0
        for i in range(len(tournoi.tours)):
            nombre_tours_ouverts += 1
            if tournoi.tours[i].statut == 'Terminé':
                nombre_tours_termines += 1
        if choix_menu == 2:
            nombre_tours = nombre_tours_ouverts
        elif choix_menu == 3:
            nombre_tours = nombre_tours_termines
        print("\n---> Choisissez le tour dans la liste ci-dessous :\n")
        for i in range(len(NOM_TOURS) - nombre_tours):
            print(f"{i + nombre_tours + 1} -- {NOM_TOURS[i + nombre_tours]}")
        print("0 -- Revenir au menu précédent")
        return nombre_tours

    def afficher_menu_editer_rapports(self):
        """Affiche le menu des rapports.
           Choix '4' du menu principal."""
        menu_rapports = {
            1: "Liste de tous les joueurs (par ordre alphabétique)",
            2: "Liste de tous les joueurs (par classement)",
            3: "Liste de tous les tournois",
            4: "Liste de tous les joueurs d'un tournoi (par ordre alphabétique)",
            5: "Liste de tous les joueurs d'un tournoi (par classement)",
            6: "Liste de tous les tours d'un tournoi",
            7: "Liste de tous les matchs d'un tournoi (avec bilan des points acquis)",
            0: "Revenir au menu principal"
            }
        system('clear')
        print("\n<--- EDITION DES RAPPORTS --->\n")
        for cle in menu_rapports.keys():
            print('\n', cle, '--', menu_rapports[cle])
        return len(menu_rapports.keys())

    def saisir_choix(self, premier_choix_menu, nombre_choix):
        """Retourne le choix de l'utilisateur dans le menu proposé."""
        try:
            choix = int(input("\nEntrez votre choix : "))
        except ValueError:
            return None
        # Si choix est un entier valide
        if choix in range(premier_choix_menu, nombre_choix) or choix == 0:
            return choix
        else:
            return None

    def saisir_reponse(self, message):
        """Saisie la réponse de l'utilisateur."""
        reponse = input(f"\n{message}")
        return reponse

    def afficher_message(self, message):
        """Affiche un message à la console"""
        print(f"\n{message}")

    def afficher_tournoi(self, tournoi):
        """Affiche les donnees d'un tournoi"""
        print(tournoi)
        input("\nTaper ENTREE pour continuer ...")

    def afficher_classement_joueur(self, joueur):
        """Affiche le classement d'un joueur"""
        print(joueur)
        input("\nTaper ENTREE pour continuer ...")

    def afficher_points_joueurs(self, tournoi, joueurs):
        """Affiche le total des points cumulés des joueurs du tournoi."""
        print("\n---> Bilan des points des joueurs :\n")
        for joueur in joueurs:
            indice = tournoi.joueurs.index(joueur)
            print(f"\nLe joueur {joueur.nom} {joueur.prenom} a {tournoi.nombre_points[indice]} points.")
        input("\nTaper ENTREE pour continuer ...")
