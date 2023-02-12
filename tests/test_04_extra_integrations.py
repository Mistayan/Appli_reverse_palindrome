import os.path
import unittest

import hypothesis
from hypothesis import strategies

from models.Clock import Clock
from src.messages import LangInterface, English, Francais
from utilities.OHCE_Builder import OHCEBuilder


class OHCETestsExtras(unittest.TestCase):
    """ Tests avancés de fonctionnalités ajoutées après le cours. """

    def test_01_langues_renseignees(self):
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

    @hypothesis.given(strategies.text(min_size=2))
    def test_02_integration_sauvegarde_fichier(self, _txt: str):
        """ Test que OHCE enregistre bien son historique à chaque utilisation """
        _time: int = Clock().time
        ohce = OHCEBuilder().prends_comme_langue(Francais).build()
        if not isinstance(_txt, str):
            self.assertRaises(ValueError, ohce.traiter(_txt))
            return
        sentance = ohce.traiter(_txt)
        root = ohce.save_dir
        self.assertTrue(os.path.exists(f"{root}{_time}"))
        with open(root, 'r') as fp:
            self.assertIn(sentance, fp.readlines())
