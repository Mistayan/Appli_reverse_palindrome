from src.models.Clock import Clock


class ClockOverride(Clock):
    """ Interface d'Override de test de Clock, afin de pouvoir en changer l'heure (tests uniquement)"""

    def __init__(self):
        super().__init__()

    def set_time(self, time):
        """ Change l'heure de l'horloge à l'heure donnée """
        self.__time = time
        return self

    @property
    def time(self):
        return self.__time
