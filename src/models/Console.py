from utils.menu_utils import do_choice_menu


class Console:

    def __init__(self, app):
        self.__app = app() or app
        self._run = False

    @property
    def __main_menu(self):
        return {
            "Lancer": self.ohce_,
            # "Options": self.options,
            "Quitter": self.quitter
        }

    def menu(self, _menu=None):
        _menu = _menu or self.__main_menu
        for i, (elem, action) in enumerate(_menu.items()):
            print(f"{i + 1} : {elem}")
        _choice = do_choice_menu(_menu)  # input
        _action = _menu.get(_choice)
        if _action:
            return _action()
        return

    def start(self):
        self._run = True
        while self._run:
            self.menu()

    def ohce_(self):
        _in = input("Entrez un chaine de characters")
        print(self.__app.traiter(_in))

    def options(self):
        pass

    def quitter(self):
        self._run = False
