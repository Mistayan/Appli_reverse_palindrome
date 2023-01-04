
class OHCE:
    def traiter(self, string: str):
        if string.lower() == "radar":
            return f"Bonjour {string[::-1]}"
        _reversed = string[::-1]
        return "Bonjour " + (string + " Bien dit!" if _reversed == string else _reversed)
        # raise NotImplementedError
