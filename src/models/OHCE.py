from messages import LangSelector


class OHCE:
    _lang = None

    def __init__(self, lang=None):
        self._lang = LangSelector(lang=lang)

    def traiter(self, string: str):
        if not isinstance(string, str):
            raise ValueError(self._lang.impossible_reverse)
        _reversed = string[::-1]
        if string.lower() == "radar":
            string = _reversed
        return self._lang.bonjour + " " + (
            string + " " + self._lang.bien_dit if _reversed == string else _reversed) \
            + " " + self._lang.au_revoir
        # raise NotImplementedError
