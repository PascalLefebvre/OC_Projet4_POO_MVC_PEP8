"""Définit les structures de données."""

from tinydb import Storage, TinyDB
import pickle

NOMBRE_JOUEURS = 8
NOM_TOURS = ("Round1", "Round2", "Round3", "Round4")
NOMBRE_TOURS = len(NOM_TOURS)
NOMBRE_MATCHS = 3
NOM_FICHIER_STOCKAGE = 'database/db.pickle'


class Donnees:
    """Classe des données."""

    def __init__(self):
        """Stocke les joueurs et les tournois."""
        self.tournois = []
        self.joueurs = []
        self.donnees_restaurees = False

    def sauvegarder(self):
        """Sauvegarde les joueurs et les tournois."""
        db = TinyDB(NOM_FICHIER_STOCKAGE, storage=StoragePickle)
        table_joueurs = db.table('joueurs')
        table_joueurs.truncate()
        for joueur in self.joueurs:
            table_joueurs.insert({'type': 'joueur', 'valeur': joueur})
        table_tournois = db.table('tournois')
        table_tournois.truncate()
        for tournoi in self.tournois:
            table_tournois.insert({'type': 'tournoi', 'valeur': tournoi})
        db.close()

    def restaurer(self):
        """Restaure les joueurs et les tournois"""
        db = TinyDB(NOM_FICHIER_STOCKAGE, storage=StoragePickle)
        table_joueurs = db.table('joueurs')
        liste_joueurs = table_joueurs.all()
        for i in range(len(liste_joueurs)):
            self.joueurs.append(liste_joueurs[i]['valeur'])
        table_tournois = db.table('tournois')
        liste_tournois = table_tournois.all()
        for i in range(len(liste_tournois)):
            self.tournois.append(liste_tournois[i]['valeur'])
        db.close()
        self.donnees_restaurees = True


class StoragePickle(Storage):
    """Définit Pickle comme procédé de (dé)serialisation des objets 'joueur' et 'tournoi'
       stockés dans la base TinyDB."""

    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, 'rb') as handle:
            try:
                donnees = pickle.load(handle)
                return donnees
            except EOFError:
                None

    def write(self, donnees):
        with open(self.filename, 'wb+') as handle:
            pickle.dump(donnees, handle)

    def close(self):
        pass
