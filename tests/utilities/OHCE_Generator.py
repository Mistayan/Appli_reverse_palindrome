from utilities.OHCE_Builder import OHCEBuilder


class OHCEGenerator:
    def __init__(self):
        pass

    def generate(self, nb_wanted: int):
        for i in range(nb_wanted):
            yield OHCEBuilder()
