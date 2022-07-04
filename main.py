"""Point d'entrée"""

from modeles.tournoi import Tournoi
from modeles.joueur import Joueur
from modeles.tour import Tour, NOM_TOURS
from modeles.match import Match

import time

NOMBRE_MATCHS = 3


def jouer_matchs(tour, paires_joueurs):
    """Crée tous les matchs d'un tours"""
    matchs = {}
    for paires in paires_joueurs:
        for i in range(NOMBRE_MATCHS):
            match = Match(paires[0], paires[1])
            resultats = match.jouer_match()
            matchs[match] = resultats
            #tour.ajouter_match(match)
    print(f"\nLes scores des matchs du {tour.nom} sont les suivants :\n")
    for cle, valeur in matchs.items():
        print(f"{cle.joueur_1.nom} contre {cle.joueur_2.nom} : {valeur}")
    return matchs

def calculer_points(matchs):
    for cle, valeur in matchs.items():
        cle.joueur_1.cumuler_points(valeur[0])
        cle.joueur_2.cumuler_points(valeur[1])

def afficher_points(tour, joueurs):
    print(f"\nBilan des points des joueurs à l'issue du {tour.nom} :\n")
    for joueur in joueurs:
        joueur.afficher_points()

def main():
    
    joueurs = [ Joueur("Dupont", "Jean", "12/11/2000", "M", 150),
                Joueur("Durand", "Pierre", "08/04/1998", "M", 200),
                Joueur("Dupuy", "Dominique", "18/08/1988", "M", 175),
                Joueur("Dutheil", "Jacques", "25/07/1993", "F", 125),
                Joueur("Dutronc", "Yves", "06/02/1980", "M", 225),
                Joueur("Duboursin", "Claude", "30/11/1978", "M", 100),
                Joueur("Dupain", "Marcel", "11/12/1962", "M", 250),
                Joueur("Duvin", "Annie", "10/05/1981", "F", 215) ]

    paires_joueurs = []
    matchs_tour = []

    tournoi = Tournoi("Echecs Challenge", "Millau", time.strftime("%a %b %d %Y"))
    print(tournoi)

    for i in range (len(NOM_TOURS)):
        tour = Tour(NOM_TOURS[i], time.asctime())
        joueurs, paires_joueurs = tour.appairer_joueurs(joueurs)
        tour.afficher_joueurs(joueurs)
        matchs_tour = jouer_matchs(tour, paires_joueurs)
        calculer_points(matchs_tour)
        afficher_points(tour, joueurs)


""" Expression du "main" en langage naturel :
    1- créer un nouveau tournoi
    2- ajouter huit joueurs
    3- générer paires de joueurs pour le premier tours
    4- entrer les résultats du premier tours
    5- répéter 3 et 4 jusqu'à ce que tous les tours soient joués
       et que tournoi soit terminé """    

if __name__ == "__main__":
    main()