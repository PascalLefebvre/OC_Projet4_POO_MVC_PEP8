"""Definit le contrôleur des menus de l'application."""

from .match import ControleurMatch
from .tour import ControleurTour
from .donnees import ControleurDonnees

class ControleurMenu:
    """Contrôleur des menus."""

    def __init__(self, vue, vue_rapports):
        """A une vue."""
        self.vue = vue
        self.vue_rapports = vue_rapports
        self.controleur_match = ControleurMatch(self.vue)
        self.controleur_tour = ControleurTour(self.vue)
        self.controleur_donnees = ControleurDonnees(self.vue)
    
    def gerer_menu_liste_tournois(self):
        """Choisit le tournoi à gérer"""
        self.vue.afficher_liste_tournois(self.controleur_donnees.tournois)
        nombre_choix = len(self.controleur_donnees.tournois)+1
        choix = self.vue.saisir_choix(nombre_choix)
        if choix == None:
            message = "Choix invalide. Merci d'entrer un chiffre entre 0 et " + str(nombre_choix-1)
            self.vue.afficher_message(message)
        else:
            return choix

    def gerer_menu_tours(self):
        # Gère le menu du choix du tour.
        choix = self.choisir_tour()
        if choix != 0:
            pass

    def gerer_menu_tournoi(self):
        """Gère le menu de gestion d'un tournoi (inscription et association des joueurs et saisie des résultats)."""
        while True:
            # Sélection du tournoi à gérer
            choix_tournoi = self.gerer_menu_liste_tournois()
            if choix_tournoi == 0:
                return
            # Décalage de "+1" entre le numéro du choix et l'indice du tournoi correspondant
            tournoi_en_cours = self.controleur_donnees.tournois[choix_tournoi-1]
            # Déclenche les actions du sous-menu de gestion d'un tournoi
            while True:
                nombre_choix = self.vue.afficher_menu_tournoi(tournoi_en_cours)
                choix = self.vue.saisir_choix(nombre_choix)
                if choix == None:
                    message = "Choix invalide. Merci d'entrer un chiffre entre 0 et " + str(nombre_choix-1)
                    self.vue.afficher_message(message)
                elif choix == 0:
                    break    
                elif choix == 1:
                    self.controleur_donnees.inscrire_joueurs(tournoi_en_cours)
                elif choix == 2:
                    tour_en_cours = self.controleur_tour.creer_tour(tournoi_en_cours)
                    self.controleur_tour.appairer_joueurs(tournoi_en_cours, tour_en_cours)
                elif choix == 3:
                    choix_tour = self.controleur_tour.choisir_tour()
                    if choix_tour != 0:
                        self.controleur_match.saisir_resultats_matchs(tournoi_en_cours, choix_tour)

    def gerer_menu_rapports(self):
        """Gère le menu d'édition des rapports."""
        while True:
            nombre_choix = self.vue.afficher_menu_rapports()
            choix = self.vue.saisir_choix(nombre_choix)
            if choix == None:
                message = "Choix invalide. Merci d'entrer un chiffre entre 0 et " + str(nombre_choix-1)
                self.vue.afficher_message(message)
            elif choix == 0:
                break             
            elif choix == 1:
                self.vue_rapports.afficher_liste_joueurs(self.controleur_donnees.joueurs, "ordre alphabetique")
            elif choix == 2:
                self.vue_rapports.afficher_liste_joueurs(self.controleur_donnees.joueurs, 'classement')
            elif choix == 3:
                self.vue_rapports.afficher_liste_tournois(self.controleur_donnees.tournois)
            else:
                while True:
                    # Sélection du tournoi
                    choix_tournoi = self.gerer_menu_liste_tournois()
                    if choix_tournoi == 0:
                        break
                    # Décalage de "+1" entre le numéro du choix et l'indice du tournoi correspondant
                    tournoi_en_cours = self.controleur_donnees.tournois[choix_tournoi-1]
                    if choix == 4:
                        self.vue_rapports.afficher_liste_joueurs(tournoi_en_cours.joueurs, "ordre alphabetique")
                    elif choix == 5:
                        self.vue_rapports.afficher_liste_joueurs(tournoi_en_cours.joueurs, "classement")
                    elif choix == 6:
                        self.vue_rapports.afficher_liste_tours(tournoi_en_cours)
                    elif choix == 7:
                        self.vue_rapports.afficher_liste_matchs(tournoi_en_cours)

    def gerer_menu_classement(self):
        """Met à jour le classement des joueurs."""
        pass

    def gerer_menu_principal(self):
        """Gère le menu principal."""
        while True:
            nombre_choix = self.vue.afficher_menu_principal()
            choix = self.vue.saisir_choix(nombre_choix)
            if choix == None:
                message = "Choix invalide. Merci d'entrer un chiffre entre 0 et " + str(nombre_choix-1)
                self.vue.afficher_message(message)
            elif choix == 0:
                message = "\n\nEtes-vous sûr de vouloir quitter l'application (o/n) ? "
                reponse = self.vue.saisir_reponse(message)
                if reponse == 'o':
                    exit()                
            elif choix == 1:
                self.controleur_donnees.creer_tournoi()
            elif choix == 2:
                self.gerer_menu_tournoi()
            elif choix == 3:
                self.gerer_menu_classement
            elif choix == 4:
                self.gerer_menu_rapports()
            elif choix == 5:
                self.controleur_donnees.sauvegarder_donnees()
            elif choix == 6:
                self.controleur_donnees.restaurer_donnees()


