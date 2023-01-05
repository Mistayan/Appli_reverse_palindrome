from __future__ import annotations

from messages import LangSelector, Francais
from models import OHCE


class OHCEBuilder:
    _lang = Francais

    def __init__(self):
        pass

    def build(self) -> OHCE.__class__:
        return OHCE(self._lang)

    def prends_comme_langue(self, lang: LangSelector) -> OHCEBuilder:
        """
        Permet d'assigner une langue à la volée
        :param lang: la langue souhaitée pour votre interface
        :return: self, permet d'utiliser des instructions chainées:  
            >>> OHCEBuilder().prends_comme_langue(Francais).build()
        """
        self._lang = lang
        return self
