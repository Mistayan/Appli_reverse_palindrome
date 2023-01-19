import unittest

from src.messages import LangInterface, English, Francais


class OHCETestsExtras(unittest.TestCase):
    """ Tests avancés de fonctionnalités ajoutées après le cours. """

    def test_etape_01(self):
        """
        Malheureusement, en python les Interfaces sont plus complexes à réaliser que dans d'autres langages
        On s'assure que les modules de langues soient tous chargés
        """
        for attribute in LangInterface().__annotations__:
            assert attribute in Francais().__annotations__
            assert attribute in English().__annotations__
