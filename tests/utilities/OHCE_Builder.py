from __future__ import annotations

from src.messages import Francais
from src.models import OHCE
from src.models.Clock import Clock
from tests.utilities.OHCE_Override import OHCEOverride


class OHCEBuilder:
    _lang = Francais()
    _time: int

    def __init__(self):
        pass

    def build(self) -> OHCE.__class__:
        ret = None
        if hasattr(self, '_time'):
            ret = OHCEOverride(lang=self._lang, time=self._time)
        else:
            ret = OHCEOverride(lang=self._lang, time=Clock().time)
        return ret

    def prends_comme_langue(self, lang) -> OHCEBuilder:
        """
        Permet d'assigner une langue à la volée:
            >>> OHCEBuilder().prends_comme_langue(Francais).build()
        :param lang: la langue souhaitée pour votre interface
        :return: self, permet d'utiliser des instructions chainées

        """
        self._lang = lang()
        return self

    def a_heure_donnee(self, time: int):
        """
        Permet d'assigner une langue à la volée:
            >>> OHCEBuilder().a_heure_donnee(8).build()
        :param time : l'heure souhaitée pour votre interface
        :return : self, permet d'utiliser des instructions chainées.
        """
        self._time = time
        return self
