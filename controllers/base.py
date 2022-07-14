"""Definit le contrôleur principal."""

import time

from models.donnees import NOMBRE_JOUEURS, NOM_TOURS, NOMBRE_MATCHS
from models.joueur import Joueur
from models.tournoi import Tournoi
from models.tour import Tour
from models.match import Match


class Controller:
    """Contrôleur principal."""

    def __init__(self, view):
        """A une vue."""
        self.view = view
        self.tournois = []

    def creer_tournoi(self):
        """Crée un tournoi."""
        nom, lieu, description, date_debut, controle_temps = self.view.saisir_tournoi()
        self.tournois.append(Tournoi(nom, lieu, description, date_debut, controle_temps))
        self.view.afficher_tournoi(self.tournois[-1])
    
    def choisir_tournoi_a_gerer(self):
        """Choisit le tournoi à gérer"""
        self.view.afficher_liste_tournois(self.tournois)
        nombre_choix = len(self.tournois)+1
        choix = self.view.saisir_choix(nombre_choix)
        if choix == None:
            print(f"\nChoix invalide. Merci d'entrer un chiffre entre 0 et {nombre_choix-1}.")
        else:
            return choix

    def inscrire_joueurs(self, tournoi):
        """Crée quelques joueurs."""
        while len(tournoi.joueurs) < NOMBRE_JOUEURS:
            nom, prenom, date_naissance, sexe, classement = self.view.saisir_joueur(len(tournoi.joueurs))
            if not nom:
                return
            joueur = Joueur(nom, prenom, date_naissance, sexe, classement)
            tournoi.ajouter_joueur(joueur)
        self.view.afficher_classement_joueurs(tournoi.joueurs)

    def choisir_tour(self):
        """Choisit le tour à gérer"""
        self.view.afficher_liste_tours()
        nombre_choix = len(NOM_TOURS)+1
        choix = self.view.saisir_choix(nombre_choix)
        if choix == None:
            print(f"\nChoix invalide. Merci d'entrer un chiffre entre 0 et {nombre_choix-1}.")
        else:
            return choix

    def creer_tour(self, tournoi, nom_tour):
        """Crée un tour."""
        tour = Tour(nom_tour, time.asctime())
        tournoi.ajouter_tour(tour)
        return tour

    def appairer_joueurs(self, tournoi, tour):
        """Associe les joueurs par paire"""
        nombre_paires_joueurs = int(len(tournoi.joueurs)/2)
        joueurs_ordonnes = []

        if tour.nom == NOM_TOURS[0]:
            # selon leur classement pour le premier tour
            joueurs_ordonnes = sorted(tournoi.joueurs, key=lambda joueur: joueur.classement, reverse=True)
            print(f"\n---> Les joueurs du {tour.nom} sont appairés selon leur classement :\n")
            for i in range(nombre_paires_joueurs):
                tour.ajouter_paire_joueurs((joueurs_ordonnes[i], joueurs_ordonnes[i+nombre_paires_joueurs]))
        else:
            # selon leurs points acquis pendant le tournoi pour les autres tours
            nombre_points = tournoi.nombre_points.copy()
            for i in range(NOMBRE_JOUEURS):
                maximum_points = 0
                for indice in range(len(nombre_points)):
                    if nombre_points[indice] > maximum_points:
                        maximum_points = nombre_points[indice]
                        indice_maximum = indice
                joueurs_ordonnes.append(tournoi.joueurs[indice_maximum])
                nombre_points[indice_maximum] = -1
            print(f"\n---> Les joueurs du {tour.nom} sont appairés selon leur nombre de points :\n")
            for i in range(0, len(tournoi.joueurs)-1, 2):
                tour.ajouter_paire_joueurs((joueurs_ordonnes[i], joueurs_ordonnes[i+1]))            
        
        for i in range(nombre_paires_joueurs):    
            print(f"{tour.paires_joueurs[i][0].nom} joue contre {tour.paires_joueurs[i][1].nom}")
        
        return joueurs_ordonnes

    def generer_paires_joueurs(self, tournoi):
        """Génère les paires de joueurs"""
        choix = self.choisir_tour()
        tour = self.creer_tour(tournoi, NOM_TOURS[choix-1])
        joueurs_ordonnes = self.appairer_joueurs(tournoi, tour)
        if tour.nom == NOM_TOURS[0]:
            self.view.afficher_classement_joueurs(joueurs_ordonnes)
        else:
            self.view.afficher_points_joueurs(joueurs_ordonnes, tournoi)

    def jouer_matchs(self, tour, paires_joueurs):
        """Crée tous les matchs d'un tour"""
        for paires in paires_joueurs:
            for i in range(NOMBRE_MATCHS):
                match = Match(paires[0], paires[1])
                match.jouer_match()
                tour.ajouter_match(match)
        print(f"\nLes scores des matchs du {tour.nom} sont les suivants :\n")
        for match in tour.matchs:
            print(f"{match.joueur_1.nom} contre {match.joueur_2.nom} : {match.joueur_score_1} à {match.joueur_score_2}")

    def calculer_points(self, tournoi, matchs):
        """Calcule les points accumulés par les joueurs lors d'un tour"""
        for match in matchs:
            tournoi.cumuler_points(match.joueur_1, match.joueur_score_1)
            tournoi.cumuler_points(match.joueur_2, match.joueur_score_2)

    def saisir_resultats_matchs(self, tournoi):
        choix = self.choisir_tour()
        tour = tournoi.tours[choix-1]
        self.jouer_matchs(tour, tour.paires_joueurs)
        self.calculer_points(tournoi, tour.matchs)
        self.view.afficher_points(tournoi, tour)

    def gerer_tournoi(self):
        """Gère un tournoi (inscription et association des joueurs et saisie des résultats"""
        # Sélection du tournoi à gérer
        choix_tournoi = self.choisir_tournoi_a_gerer()
        if choix_tournoi == 0:
            return
        # Décalage de "+1" entre le numéro du choix et l'indice du tournoi correspondant
        tournoi_en_cours = self.tournois[choix_tournoi-1]
        # Déclenche les actions du sous-menu de gestion d'un tournoi
        while True:
            nombre_choix = self.view.afficher_menu_tournoi(tournoi_en_cours)
            choix = self.view.saisir_choix(nombre_choix)
            if choix == None:
                print(f"\nChoix invalide. Merci d'entrer un chiffre entre 0 et {nombre_choix-1}.")
            elif choix == 0:
                break      
            elif choix == 1:
                self.inscrire_joueurs(tournoi_en_cours)
            elif choix == 2:
                self.generer_paires_joueurs(tournoi_en_cours)
            elif choix == 3:
                self.saisir_resultats_matchs(tournoi_en_cours)

    def gerer_menu_principal(self):
        """Déclenche les actions du menu principal en fonction du choix de l'utilisateur"""
        while True:
            nombre_choix = self.view.afficher_menu_principal()
            choix = self.view.saisir_choix(nombre_choix)
            if choix == None:
                print(f"\nChoix invalide. Merci d'entrer un chiffre entre 0 et {nombre_choix-1}.")
            elif choix == 0:
                car = input("\n\nEtes-vous sûr de vouloir quitter l'application (o/n) ? ")
                if car == 'o':
                    exit()                
            elif choix == 1:
                self.creer_tournoi()
            elif choix == 2:
                self.gerer_tournoi()
            elif choix == 3:
                pass
            elif choix == 4:
                pass
            elif choix == 5:
                pass

