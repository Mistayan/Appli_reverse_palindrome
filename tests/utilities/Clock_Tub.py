from src.models.Clock import Clock


class ClockTub(Clock):
    """ Interface de test de Clock, afin de pouvoir en changer l'heure (tests uniquement)"""

    def __init__(self):
        super().__init__()

    def set_time(self, time):
        """ Change l'heure de l'horloge à l'heure donnée """
        self._time = time
        return self
