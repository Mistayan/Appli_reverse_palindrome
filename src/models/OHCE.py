from messages import LangSelector
from models.Clock import Clock


class OHCE:
    _lang: LangSelector
    _time: int

    def __init__(self, lang=None, time=None):
        self._lang = LangSelector(lang=lang)

        print(time)
        if time is not None:
            self._time = time
        else:
            self._time = Clock().time

    @property
    def bonjour(self):
        if self._time < 6:
            msg_bonjour = self._lang.late_nighter
        elif self._time < 12:
            msg_bonjour = self._lang.bonjour
        elif self._time < 16:
            msg_bonjour = self._lang.bonjour
        elif self._time < 20:
            msg_bonjour = self._lang.bon_apres_midi
        elif self._time < 24:
            msg_bonjour = self._lang.bonsoir
        else:
            # if self._time >= 24 or self._time < 0:
            raise ValueError("Invalid Time")
        return msg_bonjour

    @property
    def au_revoir(self):
        if self._time < 6:
            msg_au_revoir = self._lang.de_bon_matin
        elif self._time < 12:
            msg_au_revoir = self._lang.bonne_journee
        elif self._time < 16:
            msg_au_revoir = self._lang.bon_apres_midi
        elif self._time < 20:
            msg_au_revoir = self._lang.bonne_soiree
        elif self._time < 22:
            msg_au_revoir = self._lang.bonne_nuit
        elif self._time < 24:
            msg_au_revoir = self._lang.vas_te_coucher
        else:
            # if _time >= 24 or _time < 0:
            raise ValueError("Invalid Time")
        return msg_au_revoir

    @staticmethod
    def string_palindrome(string: str):
        return string[::-1]

    def traiter(self, string: str):
        if not isinstance(string, str):
            raise ValueError(self._lang.impossible_reverse)
        _reversed = self.string_palindrome(string)
        if string.lower() == "radar":
            string = string[::-1]
        bien_dit = self._lang.bien_dit + '\n' if _reversed == string else ''
        return f"{self.bonjour}\n{_reversed}\n{bien_dit}{self.au_revoir}"
        # raise NotImplementedError
