from messages import LangSelector
from utils.menu_utils import faire_choix_menu


class Console:
    _lang = LangSelector()

    def __init__(self, app):
        self.__app = app() or app
        self._run = False

    @property
    def __main_menu(self):
        return {
            "Lancer": self.__ohce_,
            # "Options": self.options,
            "Quitter": self.__quitter
        }

    def __menu(self, _menu=None):
        _menu = _menu or self.__main_menu
        for i, (elem, action) in enumerate(_menu.items()):
            print(f"{i + 1} : {elem}")
        _choice = faire_choix_menu(_menu)  # input
        _action = _menu.get(_choice)
        if _action:
            return _action()
        return

    def start(self):
        self._run = True
        while self._run:
            self.__menu()

    def __ohce_(self):
        _in = input("Entrez une chaine de characters")
        print(self.__app.traiter(_in))

    def __options(self):
        pass

    def __quitter(self):
        self._run = False
