import unittest

from src.messages import LangInterface, English, Francais


class OHCETestsExtras(unittest.TestCase):
    """ Tests avancés de fonctionnalités ajoutées après le cours. """

    def test_etape_01(self):
        """
        Malheureusement, en python les Interfaces sont plus complexes à réaliser que dans d'autres langages
        On s'assure que les modules de langues ont bien tous été renseignés, en fonction de la base LangInterface
        """
        # ETANT DONNE l'interface de base des langues
        base = LangInterface().__annotations__
        # POUR CHAQUE phrase possible,
        for attribute in base:
            # CETTE phrase est-elle présente en français ?
            self.assertIn(attribute, Francais().__dir__())
            # CETTE phrase est-elle présente en english ?
            assert attribute in English().__dir__()
