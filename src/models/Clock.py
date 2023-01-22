from datetime import datetime


class Clock:
    _time: int

    def __init__(self):
        self._time = datetime.now().hour

    @property
    def time(self):
        return self._time
