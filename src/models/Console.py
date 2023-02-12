import re
from typing import Type, Dict, Any

from attr import attr


class Console:
    """ Interface CLI pour que l'utilisateur puisse interagir avec une api"""

    def __init__(self, app: Type):
        self.__app = app() or app
        self._lang = self.__app.lang  # la langue de la console est directement liée à celle de OHCE
        self._run = False

    @property
    def __main_menu(self) -> Dict[str, attr]:
        """
        Menu du menu principal
        Exporté afin de facilement pouvoir le modifier de manière conditionnelle
        :return: Le menu de base de la console, pour interagir avec l'API
        """
        return {
            self._lang.go: self.__ohce__,
            self._lang.explorer: self.__explore_app,
            self._lang.options: self.__options,
            self._lang.quitter: self.__quitter
        }

    def __menu(self, _menu=None) -> Any:
        """
        Crée un menu interactif, de longueur variable
        L'utilisateur devra faire un choix dans ce menu pour en sortir
        :param _menu: un dictionnaire de type {"message": objet}; Action peut être une méthode ou un objet.
        :return: la référence de l'action sélectionnée dans le menu (il faudra l'activer si c'est une func)
        """
        # INIT
        _menu = _menu or self.__main_menu
        # DISPLAY
        for i, (elem, action) in enumerate(_menu.items()):
            print(f"{i + 1} : {elem}")
        # CHOOSE
        _choix = self.__faire_choix_menu(_menu)  # input
        _action = _menu.get(_choix)  # Cannot be None with previous checks
        return _action

    def start(self):
        """ Lance l'interface qui devra ensuite etre quitté via le menu (ou ^C)"""
        self._run = True
        while self._run:
            self.__menu()()

    def __ohce__(self) -> None:
        """ Utilise OHCE pour répondre à l'utilisateur """
        _in = input(self._lang.ohce_in)
        print(self.__app.traiter(_in))

    def __options(self) -> None:
        """ Affiche les options de configuration de l'OHCE """
        options = self._lang.possibilities
        langue = self.__menu(options)
        self._lang.set_lang(langue())
        print(self._lang.lang_select)

    def __faire_choix_menu(self, menu: Dict[str, classmethod]) -> Any:
        """
        Demande à l'utilisateur son choix en nombre dans le menu donné
        :param menu: un menu sous forme de dictionnaire
        :return: l'action liée au choix de l'utilisateur
        """

        _choix = 0
        while not _choix:
            _in = input(self._lang.entier_in)
            try:
                _choix = int(_in)
                assert 0 < _choix <= len(menu)
            except ValueError:
                print(self._lang.not_int)
            except AssertionError:
                print(self._lang.int_invalid.format(len(menu)))
                _choix = 0
        return self.__element_du_menu_choisi(menu, _choix)

    @staticmethod
    def __element_du_menu_choisi(menu: Dict, _choix):
        for i, (k, v) in enumerate(menu.items()):
            if i + 1 == _choix:
                return k

    def __explore_app(self):
        """ Permet d'explorer les méthodes publiques de l'api connectée """
        _dir = {}
        for pub in dir(self.__app):
            if not re.match(r'(.*_+$)|(^_+.*)', pub):
                _dir.setdefault(pub, self.__app.__getattribute__(pub))
        _dir.setdefault(self._lang.retour, self.__quitter)
        print(self._lang.explorer_module)
        choix = self.__menu(_dir)
        try:
            choix = choix()
        except TypeError:
            pass
        finally:
            if choix:
                print(choix.__doc__)
                print(choix.__dir__)
                try:
                    print(choix.__annotations__)
                except AttributeError:
                    pass
            return self

    def __quitter(self):
        self._run = False
