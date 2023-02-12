import datetime
import re
import unittest

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

    # @hypothesis.given(strategies.text(min_size=2))
    def test_02_integration_sauvegarde_fichier(self):
        """ Test que OHCE enregistre bien son historique à chaque utilisation """
        # ETANT DONNE ohce en Francais
        ohce = OHCEBuilder().prends_comme_langue(Francais).build()
        # SI l'on rentre une chaine de charactère
        _txt = "test_save"
        sentence = ohce.traiter(_txt)
        # ALORS, on s'assure qu'OHCE enregistre dans un fichier à la date, heure, minute, seconde actuelle
        root = ohce.save_dir + re.sub(r":", "-", ''.join(str(datetime.datetime.now()).split('.')[0:-1]))
        # ET que le fichier contient la dernière phrase générée
        with open(root, 'r') as fp:
            self.assertIn(' '.join(sentence.split("\n") + ['\n']), fp.readlines())
