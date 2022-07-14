"""Point d'entrée"""

from controllers.base import Controller
from vues.base import Vue


def main():
    vue = Vue()
    gestion_tournoi = Controller(vue)
    gestion_tournoi.gerer_menu_principal()


if __name__ == "__main__":
    main()