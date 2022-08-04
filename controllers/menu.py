"""Definit le contrôleur des menus de l'application."""

from os import system

from .match import ControleurMatch
from .tour import ControleurTour
from .donnees import ControleurDonnees


class ControleurMenu:
    """Contrôleur des menus."""

    def __init__(self, vue, vue_rapports):
        """A deux vues : une pour la gestion des menus et une pour celle des rapports."""
        self.vue = vue
        self.vue_rapports = vue_rapports
        self.controleur_match = ControleurMatch(self.vue)
        self.controleur_tour = ControleurTour(self.vue, self.vue_rapports)
        self.controleur_donnees = ControleurDonnees(self.vue, self.vue_rapports)
        self.joueurs = self.controleur_donnees.joueurs
        self.tournois = self.controleur_donnees.tournois
        self.PREMIER_CHOIX_MENU = 0

    def gerer_menu_principal(self):
        """Gère le menu principal."""
        while True:
            nombre_choix = self.vue.afficher_menu_principal()
            choix = self.vue.saisir_choix(self.PREMIER_CHOIX_MENU, nombre_choix)
            if choix is None:
                message = "Choix invalide. Merci d'entrer un chiffre entre " + \
                          str(self.PREMIER_CHOIX_MENU) + " et " + str(nombre_choix-1)
                self.vue.saisir_reponse(message)
            elif choix == 0:
                message = "\n\nEtes-vous sûr de vouloir quitter l'application (o/n) ? "
                reponse = self.vue.saisir_reponse(message)
                if reponse == 'o':
                    exit()
            # Création d'un tournoi.
            elif choix == 1:
                self.controleur_donnees.creer_tournoi()
            # Gestion d'un tournoi.
            elif choix == 2:
                self.gerer_menu_tournoi()
            # Mise à jour du classement des joueurs.
            elif choix == 3:
                self.gerer_menu_classement()
            # Edition des rapports.
            elif choix == 4:
                self.gerer_menu_rapports()
            # Sauvegarde des joueurs et tournois dans la base de données.
            elif choix == 5:
                self.controleur_donnees.sauvegarder_donnees()
            # Restauration des joueurs et tournois depuis la base de données.
            elif choix == 6:
                self.controleur_donnees.restaurer_donnees()

    def gerer_menu_tournoi(self):
        """Gère le menu de gestion d'un tournoi :
           inscription, association des joueurs et saisie des résultats."""
        while True:
            # Sélection du tournoi à gérer.
            choix_tournoi = self.gerer_menu_liste_tournois()
            # Sortie du menu.
            if choix_tournoi == 0:
                break
            elif choix_tournoi is not None:
                # Décalage de "-1" entre le numéro du choix et l'indice du tournoi correspondant.
                tournoi_en_cours = self.tournois[choix_tournoi-1]
                # Déclenche les actions du sous-menu de gestion d'un tournoi
                while True:
                    nombre_choix = self.vue.afficher_menu_gerer_tournoi(tournoi_en_cours)
                    choix = self.vue.saisir_choix(self.PREMIER_CHOIX_MENU, nombre_choix)
                    if choix is None:
                        message = "Choix invalide. Merci d'entrer un chiffre entre " + \
                                str(self.PREMIER_CHOIX_MENU) + " et " + str(nombre_choix-1)
                        self.vue.saisir_reponse(message)
                    # Sortie du menu.
                    elif choix == 0:
                        break
                    # Inscription des joueurs à un tournoi.
                    elif choix == 1:
                        self.controleur_donnees.inscrire_joueurs(tournoi_en_cours)
                    # Affichage du menu de sélection du tour à gérer.
                    else:
                        self.gerer_menu_liste_tours(tournoi_en_cours, choix)

    def gerer_menu_liste_tournois(self):
        """Choisit le tournoi à gérer"""
        self.vue.afficher_menu_choix_tournoi(self.controleur_donnees.tournois)
        nombre_choix = len(self.tournois)+1
        choix = self.vue.saisir_choix(self.PREMIER_CHOIX_MENU, nombre_choix)
        if choix is None:
            message = "Choix invalide. Merci d'entrer un chiffre entre " + \
                      str(self.PREMIER_CHOIX_MENU) + " et " + str(nombre_choix-1) + \
                      "\nAppuyer sur ENTREE pour continuer ..."
            self.vue.saisir_reponse(message)
        return choix

    def gerer_menu_liste_tours(self, tournoi, choix):
        """Choisit le tour à gérer"""
        # Vérifie que les joueurs ont été inscrits.
        if len(tournoi.joueurs) == 0:
            message = "Merci d'inscrire les joueurs avant de démarrer le tournoi !" + \
                      "\nAppuyer sur ENTREE pour continuer ..."
            self.vue.saisir_reponse(message)
            return
        # Crée le tour et génère les paires de joueurs.
        if choix == 2:
            while True:
                choix_tour = self.controleur_tour.choisir_tour(tournoi, 2)
                # Sortie du menu.
                if choix_tour == 0:
                    break
                elif choix_tour is not None:
                    try:
                        # Crée le tour choisi et appaire les joueurs si c'est le premier tour ou,
                        # si ce n'est pas le premier tour, vérifie que le tour précédent est bien terminé.
                        if choix_tour == 1 or \
                           (len(tournoi.tours) != 0 and tournoi.tours[choix_tour-2].statut == 'Terminé'):
                            tour_en_cours = self.controleur_tour.creer_tour(tournoi, choix_tour)
                            self.controleur_tour.appairer_joueurs(tournoi, tour_en_cours)
                        else:
                            message = "Merci de respecter la chronologie d'ouverture et de clôture des tours" \
                                      + " avant d'ouvrir ce tour." + "\nAppuyer sur ENTREE pour continuer ..."
                            self.vue.saisir_reponse(message)
                    # Evite la sortie de l'application si l'utilisateur ne saisit pas le 'bon' tour.
                    except IndexError:
                        message = "Merci de respecter la chronologie d'ouverture des tours." + \
                                  "\nAppuyer sur ENTREE pour continuer ..."
                        self.vue.saisir_reponse(message)
                    break
        # Crée et joue les matchs, et saisie leur résultat.
        elif choix == 3:
            while True:
                choix_tour = self.controleur_tour.choisir_tour(tournoi, 3)
                # Sortie du menu.
                if choix_tour == 0:
                    break
                elif choix_tour is not None:
                    try:
                        # Joue les matchs si le tour choisi a été précédemment créé.
                        if len(tournoi.tours) != 0 and tournoi.tours[choix_tour-1].statut == 'Ouvert':
                            self.controleur_match.saisir_resultats_matchs(tournoi, choix_tour)
                        else:
                            message = "Merci de respecter la chronologie d'ouverture et de clôture des tours" \
                                      + " avant de fermer ce tour." + "\nAppuyer sur ENTREE pour continuer ..."
                            self.vue.saisir_reponse(message)
                    # Evite la sortie de l'application si l'utilisateur ne saisit pas le 'bon' tour.
                    except IndexError:
                        message = "Merci de respecter la chronologie de fermeture des tours." + \
                                  "\nAppuyer sur ENTREE pour continuer ..."
                        self.vue.saisir_reponse(message)
                    break

    def gerer_menu_classement(self):
        """Met à jour le classement des joueurs."""
        # Vérifie que tous les tournois sont terminés avant d'autoriser la mise à jour.
        for tournoi in self.tournois:
            if tournoi.statut == 'Ouvert':
                message = "\nLe tournoi " + tournoi.nom + " n'est pas terminé. " \
                          "La mise à jour du classement des joueurs est impossible !" \
                          "\n\nAppuyer sur ENTREE pour continuer ...\n"
                self.vue.saisir_reponse(message)
                return
        system('clear')
        message = "\n<--- MODIFICATION DU CLASSEMENT --->"
        self.vue.afficher_message(message)
        self.vue_rapports.afficher_liste_joueurs(self.joueurs, "ordre alphabetique")
        while True:
            message = "Entrez le nom du joueur ('0' pour quitter): "
            nom = self.vue.saisir_reponse(message)
            # Sortie du menu.
            if nom == '0':
                break
            joueur_trouve = False
            # Mise à jour du classement si le nom du joueur est répertorié.
            for i in range(len(self.joueurs)):
                if nom.lower() == self.joueurs[i].nom.lower():
                    joueur_trouve = True
                    self.vue.afficher_classement_joueur(self.joueurs[i])
                    while True:
                        message = "Entrez le nouveau classement : "
                        try:
                            classement = int(self.vue.saisir_reponse(message))
                        except:
                            message = "Merci d'entrer un nombre. Appuyer sur ENTREE pour continuer ..."
                            self.vue.saisir_reponse(message)
                        else:
                            self.joueurs[i].modifier_classement(classement)
                            self.vue.afficher_classement_joueur(self.joueurs[i])
                            break
                if joueur_trouve:
                    break
            else:
                message = "Le joueur " + nom + " est inconnu !!!\n\nAppuyer sur ENTREE pour continuer ...\n"
                self.vue.saisir_reponse(message)

    def gerer_menu_rapports(self):
        """Gère le menu d'édition des rapports."""
        while True:
            nombre_choix = self.vue.afficher_menu_editer_rapports()
            choix = self.vue.saisir_choix(self.PREMIER_CHOIX_MENU, nombre_choix)
            if choix is None:
                message = "Choix invalide. Merci d'entrer un chiffre entre " + \
                        str(self.PREMIER_CHOIX_MENU) + " et " + str(nombre_choix-1)
                self.vue.saisir_reponse(message)
            # Sortie du menu.
            elif choix == 0:
                break
            elif choix == 1:
                self.vue_rapports.afficher_liste_joueurs(self.joueurs, "ordre alphabetique")
            elif choix == 2:
                self.vue_rapports.afficher_liste_joueurs(self.joueurs, 'classement')
            elif choix == 3:
                self.vue_rapports.afficher_liste_tournois(self.tournois)
            else:
                while True:
                    # Sélection du tournoi.
                    choix_tournoi = self.gerer_menu_liste_tournois()
                    if choix_tournoi == 0:
                        break
                    # Décalage de "-1" entre le numéro du choix et l'indice du tournoi correspondant.
                    if choix_tournoi is not None:
                        tournoi_en_cours = self.tournois[choix_tournoi-1]
                        if choix == 4:
                            self.vue_rapports.afficher_liste_joueurs(tournoi_en_cours.joueurs, "ordre alphabetique")
                        elif choix == 5:
                            self.vue_rapports.afficher_liste_joueurs(tournoi_en_cours.joueurs, "classement")
                        elif choix == 6:
                            self.vue_rapports.afficher_liste_tours(tournoi_en_cours)
                        elif choix == 7:
                            self.vue_rapports.afficher_liste_matchs(tournoi_en_cours)
                            self.vue.afficher_points_joueurs(tournoi_en_cours, tournoi_en_cours.joueurs)
