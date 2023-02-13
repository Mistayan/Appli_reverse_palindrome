from datetime import datetime


class Iclock:
    pass


class Clock(Iclock):
    __time: int

    def __init__(self):
        self.__time = datetime.now().hour

    @property
    def time(self):
        return self.__time
