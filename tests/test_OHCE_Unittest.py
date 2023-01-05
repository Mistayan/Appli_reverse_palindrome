import unittest

from src.messages.LangInterface import LangInterface as Expressions
from src.models.OHCE import OHCE


class TestOHCE(unittest.TestCase):
    def test_miroir(self):
        """ Quand on saisit une chaine, alors, celle-ci est renvoyée en miroir """
        # Etant donné l'OHCE
        ohce = OHCE()
        # quand on saisit une chaine,
        _in = "toto"

        # Alors celle-ci est renvoyée en miroir
        val = ohce.traiter(_in)
        self.assertEqual(Expressions.msgs.bonjour + " otot " + Expressions.msgs.au_revoir, val)

    def test_palindrome(self):
        """ Quand on saisit un palindrome, alors, on renvoie le palindrome, ET "Bien dit!" """
        # Etant donné l'OHCE
        ohce = OHCE()

        # quand on saisit une chaine,
        _in = "toot"
        # Alors celle-ci est renvoyée en miroir
        val = ohce.traiter(_in)
        self.assertEqual(Expressions.msgs.bonjour + " " + "toot" + " " + Expressions.msgs.bien_dit +
                         " " + Expressions.msgs.au_revoir, ohce.traiter(_in))

    def test_radar(self):
        # THEORY
        """ Test que OHCE renvoi radar """
        ohce = OHCE()

        _in = "radar"
        self.assertEqual(Expressions.msgs.bonjour + " " + "radar" + " " + Expressions.msgs.bien_dit
                         + " " + Expressions.msgs.au_revoir, ohce.traiter(_in))
        _in = "Radar"
        self.assertEqual(Expressions.msgs.bonjour + " " + "radaR" + " " + Expressions.msgs.bien_dit
                         + " " + Expressions.msgs.au_revoir, ohce.traiter(_in))

    def test_au_revoir(self):
        """ Test l'existence du message d'au revoir """
        ohce = OHCE()

        _in = "tEstS"
        self.assertEqual(Expressions.msgs.bonjour + " " + "StsEt" + " " + Expressions.msgs.au_revoir, ohce.traiter(_in))

    def test_invalid_in(self):
        ohce = OHCE()

        _in = 12
        self.assertRaises(ValueError, ohce.traiter, _in)
