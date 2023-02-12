from src.messages import LangInterface
from src.models import OHCE


class OHCEOverride(OHCE):
    """ Création d'un Override afin que l'utilisateur ne puisse plus changer l'heure dans l'application.
    Seulement les tests ont cette possibilité, grâce à cette classe"""

    def __init__(self, lang: LangInterface, time: int):
        """ Instancie l'OHCE à la langue choisie. Utilise une passerelle d'héritage pour modifier son heure"""
        super().__init__(lang=lang)
        self.__set_time(time)

    def __set_time(self, time: int):
        """set time to given value"""
        self._time = time
