"""Définit un tour (une ronde)"""


NOM_TOURS = ("Round1", "Round2", "Round3", "Round4")

class Tour:
    """Classe Tour
    
       nom    = "Round1" ou "Round2" ou etc."""

    def __init__(self, nom, date_heure_debut):
        self.nom = nom
        self.date_heure_debut = date_heure_debut


    def appairer_joueurs(self, joueurs):
        """Associe les joueurs par paire"""
        paires_joueurs = []
        NOMBRE_PAIRES_JOUEURS = int(len(joueurs)/2)

        if self.nom == NOM_TOURS[0]:
            """selon leur classement pour le premier tour"""
            joueurs = sorted(joueurs, key=lambda joueur: joueur.classement, reverse=True)
            print(f"\nLes joueurs du {self.nom} sont appairés selon leur classement :\n")
            for i in range(NOMBRE_PAIRES_JOUEURS):
                paires_joueurs.append((joueurs[i], joueurs[i+NOMBRE_PAIRES_JOUEURS]))
        else:
            """selon leurs points acquis pendant le tournoi pour les autres tours"""
            joueurs = sorted(joueurs, key=lambda joueur: joueur.nombre_points, reverse=True)
            print(f"\nLes joueurs du {self.nom} sont appairés selon leur nombre de points :\n")
            for i in range(0, len(joueurs)-1, 2):
                paires_joueurs.append((joueurs[i], joueurs[i+1]))            
        
        for i in range(NOMBRE_PAIRES_JOUEURS):    
            print(f"{paires_joueurs[i][0].nom} joue contre {paires_joueurs[i][1].nom}")
        
        return joueurs, paires_joueurs


    def afficher_joueurs(self, joueurs):
        
        print(f"\nLes joueurs participant au {self.nom} qui débute le {self.date_heure_debut} sont :\n")
        
        for joueur in joueurs:
            if self.nom == NOM_TOURS[0]:
                joueur.afficher_classement()
            else:
                joueur.afficher_points()
