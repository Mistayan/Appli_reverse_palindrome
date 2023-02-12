from src.messages import LangSelector
from src.models.Clock import Clock


class OHCE:
    """
    OHCE est une 'api' simple prenant en considération la langue de l'utilisateur et l'heure pour répondre
    C'est avant tout une gymnastique d'ajout de modules indépendants (Clock, LangSelector, ...)
    Ces modules doivent pouvoir être échangés avec des modules ayant des attributs publiques similaires.
    Cette 'api' est faite pour être utilisé en duo avec une INTERFACE (CLI, Graphique, DB, ...)
    """
    _lang: LangSelector
    _time: int

    def __init__(self, lang=None):
        """
        Instancie la classe avec la langue et/ou l'heure choisie
        Une heure invalide forcera l'heure du système
        Une langue Invalide forera le français
        :param lang: La langue de l'interface
        """
        self._lang = LangSelector(lang=lang)
        self.__clock = Clock()
        self._time = self.__clock.time

    @property
    def bonjour(self):
        """
        :return: la phrase de bonjour associée à l'heure et la langue
        :raises: ValueError
        """
        _dict = {
            # Avant HEURE, affiche TEXTE
            6: self._lang.late_nighter,
            16: self._lang.bonjour,
            20: self._lang.bon_apres_midi,
            24: self._lang.bonsoir,
        }
        return self.__message_depend_d_heure(_dict)

    @property
    def au_revoir(self):
        """
        :return: la phrase d'au revoir associée à l'heure et la langue
        :raises: ValueError
        """
        _dict = {
            # Avant HEURE, affiche TEXTE
            6: self._lang.de_bon_matin,
            12: self._lang.bonne_journee,
            16: self._lang.bon_apres_midi,
            20: self._lang.bonne_soiree,
            22: self._lang.bonne_nuit,
            24: self._lang.vas_te_coucher,
        }
        return self.__message_depend_d_heure(_dict)

    def __message_depend_d_heure(self, _dict: dict) -> str:
        """
        En fonction du dictionnaire reçu et de l'heure actuelle, renvoi le message adapté
        :param _dict: un dict contenant une heure associée à un message
        :return: le message associé à l'heure actuelle
        :raises: ValueError
        """
        if not 0 <= self._time < 24:
            self._time = self.__clock.time
        for heure, texte in _dict.items():
            if 0 <= self._time < heure:
                return texte
        raise ValueError("Invalid Time")

    @staticmethod
    def miroir(string: str):
        """ Retourne une chaine de characters en miroir """
        return string[::-1]

    def traiter(self, string: str):
        """
        Prend une chaine en entrée et l'inverse.
        Ce miroir est intégré dans une phrase contextuelle,
        disant bonjour en fonction de la langue de OHCE et de l'heure.
        :param string: la chaine qui sera inversée
        :return: une phrase contextuelle contenant la chaine inversée.
        """
        if not isinstance(string, str):
            raise ValueError(self._lang.impossible_reverse)
        _reversed = self.miroir(string)
        if string.lower() == "radar":
            string = string[::-1]
        bien_dit = self._lang.bien_dit + '\n' if _reversed == string else ''
        return f"{self.bonjour}\n{_reversed}\n{bien_dit}{self.au_revoir}"

    @property
    def lang(self):
        """ Retourne la référence du sélecteur de langue, afin de pouvoir la modifier """
        return self._lang
