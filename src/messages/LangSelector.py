import locale

from src.messages import LangInterface
from src.messages.English import English
from src.messages.Francais import Francais


class LangSelector:
    """
     Interface de sélection de langue (l'utilisateur peut changer de langue).
     Par défaut, la langue de l'os est instanciée
     """
    __lang = None
    _msgs: LangInterface = None

    def __init__(self, lang=None):
        """
        :param lang: isinstance(LangInterface, lang)
        """
        if lang:
            self._msgs = lang() or lang  # Instantiate if it has not been passed instantiated
        else:
            lang, formatting = locale.getlocale()  # WINDOWS FORMAT : English_Great Britain
            try:
                self.__lang = lang.split('_')[0]
            except:
                self.__lang = None

            match self.__lang:
                case "English":
                    self._msgs = English()
                case _:  # Défaut
                    self._msgs = Francais()

    @property
    def possibilities(self):
        return {
            "FR": Francais,
            "EN": English,
        }

    def set_lang(self, _lang):
        """
         Définit la langue du sélecteur, par une action utilisateur
        :param _lang: la langue sélectionnée par l'utilisateur, dans l'interface
        :return: la phrase de sélection de la langue choisie
        """
        self._msgs = _lang() or _lang
        return self._msgs.lang_select

    def __getattr__(self, item) -> str:
        """ Permet de récupérer les messages d'une langue (ayant la même nomination au travers des langues)"""
        if self._msgs:
            return self._msgs.__getattribute__(item)
        raise AttributeError
