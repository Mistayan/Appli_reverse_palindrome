from src.messages.LangInterface import LangInterface as Lng_


class OHCE:

    @staticmethod
    def traiter(string: str):
        if not isinstance(string, str):
            raise ValueError(Lng_.msgs.impossible)
        _reversed = string[::-1]
        if string.lower() == "radar":
            string = _reversed
        return Lng_.msgs.bonjour + " " + (
            string + " " + Lng_.msgs.bien_dit if _reversed == string else _reversed) \
            + " " + Lng_.msgs.au_revoir
        # raise NotImplementedError
