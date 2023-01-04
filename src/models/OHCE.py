from src.messages.Expressions import Expressions


class OHCE:

    def goodbye(self):
        return Expressions.au_revoir

    def traiter(self, string: str):
        if not isinstance(string, str):
            raise ValueError("Cannot reverse this")
        _reversed = string[::-1]
        if string.lower() == "radar":
            string = _reversed
        return "Bonjour " + (
            string + " Bien dit!" if _reversed == string else _reversed)\
            + " " + self.goodbye()
        # raise NotImplementedError
