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
        self.assertEqual(Expressions.bonjour + " otot " + Expressions.au_revoir, val)

    def test_palindrome(self):
        """ Quand on saisit un palindrome, alors, on renvoie le palindrome, ET "Bien dit!" """
        # Etant donné l'OHCE
        ohce = OHCE()

        # quand on saisit une chaine,
        _in = "toot"
        # Alors celle-ci est renvoyée en miroir
        val = ohce.traiter(_in)
        self.assertEqual(Expressions.bonjour + " " + "toot" + " " + Expressions.bien_dit +
                         " " + Expressions.au_revoir, ohce.traiter(_in))

    def test_radar(self):
        # THEORY
        """ Test que OHCE renvoi radar """
        ohce = OHCE()

        _in = "radar"
        self.assertEqual(Expressions.bonjour + " " + "radar" + " " + Expressions.bien_dit
                         + " " + Expressions.au_revoir, ohce.traiter(_in))
        _in = "Radar"
        self.assertEqual(Expressions.bonjour + " " + "radaR" + " " + Expressions.bien_dit
                         + " " + Expressions.au_revoir, ohce.traiter(_in))

    def test_au_revoir(self):
        """ Test l'existence du message d'au revoir """
        ohce = OHCE()

        _in = "tEstS"
        self.assertEqual(Expressions.bonjour + " " + "StsEt" + " " + Expressions.au_revoir, ohce.traiter(_in))

    def test_invalid_in(self):
        ohce = OHCE()

        _in = 12
        self.assertRaises(ValueError, ohce.traiter, _in)
