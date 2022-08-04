"""Definit le contrôleur des joueurs."""

from models.donnees import NOMBRE_JOUEURS
from models.joueur import Joueur


class ControleurJoueur:
    """Inscrit les joueurs."""

    def __init__(self, vue, vue_rapports, joueurs):
        self.vue = vue
        self.vue_rapports = vue_rapports
        self.joueurs = joueurs

    def inscrire_joueurs(self, tournoi):
        """Inscrit quelques joueurs."""
        if len(tournoi.joueurs) == NOMBRE_JOUEURS:
            message = "\nLes joueurs sont déjà inscrits.\n\nAppuyer sur ENTREE pour continuer... "
            self.vue.saisir_reponse(message)
            return
        message = "\n<-- INSCRIPTION au " + tournoi.nom + " de " + tournoi.lieu + " -->"
        self.vue.afficher_message(message)
        # Utiliser pour faciliter l'inscription à partir des joueurs déjà répertoriés.
        self.vue_rapports.afficher_liste_joueurs(self.joueurs, "ordre alphabetique")
        while len(tournoi.joueurs) < NOMBRE_JOUEURS:
            joueur_inscrit = None
            # Vérifie que la saisie du nom est correcte.
            while True:
                message = "Entrez le nom du joueur à inscrire (" + str(len(tournoi.joueurs)+1) \
                        + "/" + str(NOMBRE_JOUEURS) + "): "
                nom = self.vue.saisir_reponse(message).capitalize()
                if not nom.isalpha():
                    message = "Le nom ne doit contenir que des lettres ! Appuyer sur ENTREE pour continuer ..."
                    self.vue.saisir_reponse(message)
                else:
                    break
            # Recherche de l'existence d'un joueur et inscription de celui-ci si trouvé.
            for i in range(len(self.joueurs)):
                if nom.lower() == self.joueurs[i].nom.lower():
                    joueur_inscrit = self.joueurs[i]
                    message = "Ce joueur est déjà répertorié ..."
                    self.vue.afficher_message(message)
                    break
            if joueur_inscrit is None:
                message = "Ce joueur n'est pas répertorié ..."
                self.vue.afficher_message(message)
                prenom, date_naissance, sexe, classement = self.vue.saisir_joueur()
                joueur_inscrit = Joueur(nom, prenom, date_naissance, sexe, classement)
                self.joueurs.append(joueur_inscrit)
            tournoi.ajouter_joueur(joueur_inscrit)
            message = "Le joueur " + joueur_inscrit.nom + ' ' + joueur_inscrit.prenom \
                      + " est inscrit au " + tournoi.nom + ' de ' + tournoi.lieu
            self.vue.saisir_reponse(message)
