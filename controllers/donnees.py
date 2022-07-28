"""Definit le contrôleur des données."""

from tinydb import TinyDB

from models.donnees import NOMBRE_JOUEURS, NOM_FICHIER_STOCKAGE # joueurs
from models.joueur import Joueur
from models.tournoi import Tournoi
from utils.storage import StoragePickle

class ControleurDonnees:
    """Contrôleur des données."""

    def __init__(self, view):
        """A une vue."""
        self.view = view
        self.tournois = []
        self.joueurs = []

    def creer_tournoi(self):
        """Crée un tournoi."""
        nom, lieu, description, date_debut, controle_temps = self.view.saisir_tournoi()
        self.tournois.append(Tournoi(nom, lieu, description, date_debut, controle_temps))
        self.view.afficher_tournoi(self.tournois[-1])

    def inscrire_joueurs(self, tournoi):
        """Inscrit quelques joueurs."""
        while len(tournoi.joueurs) < NOMBRE_JOUEURS:
            nom, prenom, date_naissance, sexe, classement = self.view.saisir_joueur(len(tournoi.joueurs))
            if not nom:
                return
            joueur = Joueur(nom, prenom, date_naissance, sexe, classement)
            tournoi.ajouter_joueur(joueur)
        self.view.afficher_classement_joueurs(tournoi.joueurs)

    def sauvegarder_donnees(self):
        """Sauvegarde les joueurs et les tournois."""
        # self.initialiser_liste_joueurs()
        db = TinyDB(NOM_FICHIER_STOCKAGE, storage=StoragePickle)
        table_joueurs = db.table('joueurs')
        table_joueurs.truncate()
        for joueur in self.joueurs:
            table_joueurs.insert({'type' : 'joueur', 'valeur' : joueur})
        table_tournois = db.table('tournois')
        table_tournois.truncate()
        for tournoi in self.tournois:
            table_tournois.insert({'type' : 'tournoi', 'valeur' : tournoi})
        db.close()
        message = "Sauvegarde effectuée"
        self.view.afficher_message(message)
        input("Continuer ...")

    def restaurer_donnees(self):
        """Restaure les joueurs et les tournois"""
        db = TinyDB(NOM_FICHIER_STOCKAGE, storage=StoragePickle)
        table_joueurs = db.table('joueurs')
        liste_joueurs = table_joueurs.all()
        for i in range(len(liste_joueurs)):
            self.joueurs.append(liste_joueurs[i]['valeur'])
            print(self.joueurs[i].nom)
        table_tournois = db.table('tournois')
        liste_tournois = table_tournois.all()
        for i in range(len(liste_tournois)):
            self.tournois.append(liste_tournois[i]['valeur'])
            print(self.tournois[i].nom)
        db.close()
        input("Continuer ...")

    """def initialiser_liste_joueurs(self):
        # Initialise la liste des joueurs ayant déjà participé à un tournoi
        for i in range(len(joueurs)):
            nom = joueurs[i][0]
            prenom = joueurs[i][1]
            date_naissance = joueurs[i][2]
            sexe = joueurs[i][3]
            classement = joueurs[i][4]
            self.joueurs.append(Joueur(nom, prenom, date_naissance, sexe, classement))"""
