import locale

from messages import LangInterface
from src.messages.English import English
from src.messages.Francais import Francais


class LangSelector:
    """
     Interface de sélection de langue (l'utilisateur peut changer de langue).
     Par défaut, la langue de l'os est instanciée
     """
    __lang = None
    msgs: LangInterface = None

    def __init__(self, lang=None):
        """
        :param lang: lang doit être
        """
        if lang:
            self.msgs = lang() or lang
        else:
            lang, formatting = locale.getlocale()
            self.__lang = lang
            match self.__lang:
                case "English_United States":
                    self.msgs = English()
                case "English_Great Britain":
                    self.msgs = English()
                case _:
                    self.msgs = Francais()

    def __getattr__(self, item):
        """ Permet de récupérer les messages d'une langue (ayant la même nomination au travers des langues)"""
        if self.msgs:
            return self.msgs.__getattribute__(item)
        raise AttributeError
