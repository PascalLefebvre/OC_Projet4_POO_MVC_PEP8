"""Point d'entrée"""

# from controllers.base import Controleur
from controllers.menu import ControleurMenu
from vues.base import Vue


def main():
    vue = Vue()
    gestion_tournoi = ControleurMenu(vue)
    gestion_tournoi.gerer_menu_principal()


if __name__ == "__main__":
    main()