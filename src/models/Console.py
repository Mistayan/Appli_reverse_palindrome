from attr import attr

from src.utils.menu_utils import faire_choix_menu


class Console:

    def __init__(self, app):
        self.__app = app() or app
        self._lang = self.__app.lang  # la langue de la console est directement liée à celle de OHCE
        self._run = False

    @property
    def __main_menu(self) -> dict[str, attr]:
        """
        Menu du menu principal
        Exporté afin de facilement pouvoir le modifier de manière conditionnelle
        :return:
        """
        return {
            "GO": self.__ohce__,
            "Options": self.__options,
            "Quitter": self.__quitter
        }

    def __menu(self, _menu=None):
        """
        Crée un menu interactif, de longueur variable
        L'utilisateur devra faire un choix dans ce menu pour en sortir
        :param _menu: un dictionnaire de type {"message": objet}; Action peut être une méthode ou un objet.
        :return: l'action sélectionnée dans le menu
        """
        # INIT
        _menu = _menu or self.__main_menu
        # DISPLAY
        for i, (elem, action) in enumerate(_menu.items()):
            print(f"{i + 1} : {elem}")
        # CHOOSE
        _choix = faire_choix_menu(_menu)  # input
        _action = _menu.get(_choix)  # Cannot be None with previous checks
        return _action()

    def start(self):
        self._run = True
        while self._run:
            self.__menu()

    def __ohce__(self):
        _in = input("Entrez une chaine de characters")
        print(self.__app.traiter(_in))

    def __options(self):
        """ Affiche les options de configuration de l'OHCE """
        options = self._lang.possibilities
        langue = self.__menu(options)
        self._lang.set_lang(langue)
        print(self._lang.lang_select)

    def __quitter(self):
        self._run = False
