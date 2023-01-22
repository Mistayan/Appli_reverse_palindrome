import unittest

from parameterized import parameterized

from utilities.OHCE_Builder import OHCEBuilder


class OHCEFoundBugsTests(unittest.TestCase):

    @parameterized.expand([
        [-1, ],
        [25, ]
    ])
    def test_cas_heure_invalide(self, _heure):
        """ Assure l'impossibilité d'utiliser des heures erroné """
        # Le client a constaté lors de cas inattendus que l'<heure> pouvait dépasser 24 ou être sous 0.
        # Son souhait est que cela n'arrête pas le programme, et que l'heure soit actualisée

        # ETANT DONNE OHCE à <Heure> invalide
        ohce = OHCEBuilder().a_heure_donnee(_heure).build()

        # ALORS, on utilisera l'heure actuelle pour substituer, permettant d'enlever les erreurs.
        print(ohce.traiter("pp"))
