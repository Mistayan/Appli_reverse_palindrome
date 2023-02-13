from src.models.Clock import Clock, Iclock


class ClockMock(Iclock):
    """ Interface d'Override de test de Clock, afin de pouvoir en changer l'heure (tests uniquement)"""

    def __init__(self, time: int):
        super().__init__()
        self.__time = time

    @property
    def time(self):
        return self.__time
