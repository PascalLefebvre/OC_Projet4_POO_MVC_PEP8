"""Definit le contrôleur des données."""

from tinydb import TinyDB

from models.donnees import NOMBRE_JOUEURS, NOM_FICHIER_STOCKAGE # joueurs
from models.joueur import Joueur
from models.tournoi import Tournoi
from utils.storage import StoragePickle

class ControleurDonnees:
    """Contrôleur des données."""

    def __init__(self, vue, vue_rapports):
        """A une vue."""
        self.vue = vue
        self.vue_rapports = vue_rapports
        self.tournois = []
        self.joueurs = []

    def creer_tournoi(self):
        """Crée un tournoi."""
        nom, lieu, description, date_debut, date_fin, controle_temps = self.vue.saisir_tournoi()
        self.tournois.append(Tournoi(nom, lieu, description, date_debut, date_fin, controle_temps))
        self.vue.afficher_tournoi(self.tournois[-1])

    def inscrire_joueurs(self, tournoi):
        """Inscrit quelques joueurs."""
        if len(tournoi.joueurs) == NOMBRE_JOUEURS:
            message = "\nLes joueurs sont déjà inscrits.\n\nAppuyer sur ENTREE pour continuer... "
            self.vue.saisir_reponse(message)
            return
        message = "\n<-- INSCRIPTION au " + tournoi.nom + " de " + tournoi.lieu + " -->"
        self.vue.afficher_message(message)
        self.vue_rapports.afficher_liste_joueurs(self.joueurs, "ordre alphabetique")
        while len(tournoi.joueurs) < NOMBRE_JOUEURS:
            joueur_inscrit = None
            message = "\nEntrez le nom du joueur à inscrire : "
            nom = self.vue.saisir_reponse(message)
            for i in range(len(self.joueurs)):
                if nom.lower() == self.joueurs[i].nom.lower():
                    joueur_inscrit = self.joueurs[i]
                    message = "Ce joueur est déjà répertorié ..."
                    self.vue.afficher_message(message)
                    break
            if joueur_inscrit == None:
                    message = "Ce joueur n'est pas répertorié ..."
                    self.vue.afficher_message(message)
                    nom, prenom, date_naissance, sexe, classement = self.vue.saisir_joueur()
                    joueur_inscrit = Joueur(nom, prenom, date_naissance, sexe, classement)
                    self.joueurs.append(joueur_inscrit)
            tournoi.ajouter_joueur(joueur_inscrit)
            message = "Le joueur " + joueur_inscrit.nom + ' ' + joueur_inscrit.prenom \
                        + " est inscrit au " + tournoi.nom + ' de ' + tournoi.lieu
            self.vue.saisir_reponse(message)

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
        message = "\nSauvegarde effectuée ...\n\nAppuyer sur ENTREE pour continuer ..."
        self.vue.saisir_reponse(message)

    def restaurer_donnees(self):
        """Restaure les joueurs et les tournois"""
        db = TinyDB(NOM_FICHIER_STOCKAGE, storage=StoragePickle)
        table_joueurs = db.table('joueurs')
        liste_joueurs = table_joueurs.all()
        for i in range(len(liste_joueurs)):
            self.joueurs.append(liste_joueurs[i]['valeur'])
            # print(self.joueurs[i].nom)
        table_tournois = db.table('tournois')
        liste_tournois = table_tournois.all()
        for i in range(len(liste_tournois)):
            self.tournois.append(liste_tournois[i]['valeur'])
            # print(self.tournois[i].nom)
        db.close()
        message = "\nRestauration effectuée ...\n\nAppuyer sur ENTREE pour continuer ..."
        self.vue.saisir_reponse(message)

    """
    # Utiliser uniquement pour faciliter la création de la base de données initiale
    def initialiser_liste_joueurs(self):
        # Initialise la liste des joueurs ayant déjà participé à un tournoi
        for i in range(len(joueurs)):
            nom = joueurs[i][0]
            prenom = joueurs[i][1]
            date_naissance = joueurs[i][2]
            sexe = joueurs[i][3]
            classement = joueurs[i][4]
            self.joueurs.append(Joueur(nom, prenom, date_naissance, sexe, classement))
    """
