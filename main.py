"""Point d'entrée"""

from controllers.menu import ControleurMenu
from vues.base import Vue
from vues.rapports import VueRapports


def main():
    gestion_tournoi = ControleurMenu(Vue(), VueRapports())
    gestion_tournoi.gerer_menu_principal()


if __name__ == "__main__":
    main()