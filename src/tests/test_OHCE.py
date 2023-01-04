import unittest

from src.models.OHCE import OHCE
from src.messages.Expressions import Expressions


class TestOHCE(unittest.TestCase):
    def test_miroir(self):
        """ Quand on saisit une chaine, alors, celle-ci est renvoyée en miroir """
        # Etant donné l'OHCE
        ohce = OHCE()
        # quand on saisit une chaine,
        _in = "toto"

        # Alors celle-ci est renvoyée en miroir
        val = ohce.traiter(_in)
        self.assertEqual("Bonjour otot", val)

    def test_palindrome(self):
        """ Quand on saisit un palindrome, alors, on renvoit le palindrome, ET "Bien dit!" """
        # Etant donné l'OHCE
        ohce = OHCE()

        # quand on saisit une chaine,
        _in = "toot"
        # Alors celle-ci est renvoyée en miroir
        val = ohce.traiter(_in)
        self.assertEqual("Bonjour " + "toot" + " Bien dit!", val)

    def test_radar(self):
        # THEORY
        """ Test que OHCE renvoi radar """
        ohce = OHCE()

        _in ="radar"
        self.assertEqual("Bonjour " + "radar", ohce.traiter(_in))
        _in ="Radar"
        self.assertEqual("Bonjour " + "radaR", ohce.traiter(_in))
