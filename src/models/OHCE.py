from src.messages import LangSelector
from src.models.Clock import Clock


class OHCE:
    _lang: LangSelector
    _time: int

    def __init__(self, lang=None, time=None):
        self._lang = LangSelector(lang=lang)
        if isinstance(time, (int, float)) and 0 <= time < 24:
            self._time = time
        else:
            self._time = Clock().time

    @property
    def bonjour(self):
        _dict = {
            # Avant HEURE, affiche TEXTE
            6: self._lang.late_nighter,
            12: self._lang.bonjour,
            16: self._lang.bonjour,
            20: self._lang.bon_apres_midi,
            24: self._lang.bonsoir,
        }
        return self.__message_depend_d_heure(_dict)

    @property
    def au_revoir(self):
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
        """ En fonction du dictionnaire reçu et de l'heure actuelle, renvoi le message adapté"""
        for heure, texte in _dict.items():
            if 0 <= self._time < heure:
                return texte
        raise ValueError("Invalid Time")

    @staticmethod
    def miroir(string: str):
        return string[::-1]

    def traiter(self, string: str):
        if not isinstance(string, str):
            raise ValueError(self._lang.impossible_reverse)
        _reversed = self.miroir(string)
        if string.lower() == "radar":
            string = string[::-1]
        bien_dit = self._lang.bien_dit + '\n' if _reversed == string else ''
        return f"{self.bonjour}\n{_reversed}\n{bien_dit}{self.au_revoir}"

    @property
    def lang(self):
        return self._lang
