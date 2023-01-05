from messages import LangSelector
from utilities.OHCE_Builder import OHCEBuilder


class OHCEGenerator:
    def __init__(self):
        pass

    def generate(self, nb_wanted: int, lang: LangSelector):
        for i in range(nb_wanted):
            yield OHCEBuilder
