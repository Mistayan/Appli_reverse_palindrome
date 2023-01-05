import os
import unittest

from messages import LangSelector
from src.models.OHCE import OHCE


class TestOHCE(unittest.TestCase):
    def test_miroir(self):
        """ Quand on saisit une chaine, alors, celle-ci est renvoyée en miroir """
        # Etant donné l'OHCE
        ohce = OHCE()
        lang = ohce._lang

        # quand on saisit une chaine,
        _in = "toto"

        # Alors celle-ci est renvoyée en miroir
        val = ohce.traiter(_in)
        self.assertEqual(lang.bonjour + " otot " + lang.au_revoir, val)

    def test_palindrome(self):
        """ Quand on saisit un palindrome, alors, on renvoie le palindrome, ET "Bien dit!" """
        # Etant donné l'OHCE
        ohce = OHCE()
        lang = ohce._lang

        # quand on saisit une chaine,
        _in = "toot"
        val = ohce.traiter(_in)

        # Alors celle-ci est renvoyée en miroir
        self.assertEqual(lang.bonjour + " " + "toot" + " " + lang.bien_dit +
                         " " + lang.au_revoir, val)

    def test_radar(self):
        # THEORY
        """ Test que OHCE renvoi radar """
        ohce = OHCE()
        lang = ohce._lang

        _in = "radar"
        self.assertEqual(lang.bonjour + " " + "radar" + " " + lang.bien_dit
                         + " " + lang.au_revoir, ohce.traiter(_in))
        _in = "Radar"
        self.assertEqual(lang.bonjour + " " + "radaR" + " " + lang.bien_dit
                         + " " + lang.au_revoir, ohce.traiter(_in))

    def test_au_revoir(self):
        """ Test l'existence du message d'au revoir """
        ohce = OHCE()
        lang = ohce._lang
        _in = "tEstS"
        self.assertEqual(lang.bonjour + " " + "StsEt" + " " + lang.au_revoir, ohce.traiter(_in))

    def test_invalid_in(self):
        """ Test des entrés invalide """
        ohce = OHCE()

        self.assertRaises(ValueError, ohce.traiter, 42)
        self.assertRaises(ValueError, ohce.traiter, self)
        self.assertRaises(ValueError, ohce.traiter, 1.42)
        self.assertRaises(ValueError, ohce.traiter, os)

    from messages import English, Francais

    def test_multilingual_english(self, lang=English):
        print(lang)
        ohce = OHCE(lang=lang)
        print(ohce._lang)
        self.assertEqual(lang.bonjour + " " + "YEH!" + " " + lang.au_revoir, ohce.traiter("!HEY"))
        self.assertEqual(lang.bonjour + " " + "YEY" + " " + lang.bien_dit + " " + lang.au_revoir, ohce.traiter("YEY"))

    def test_multilingual_french(self, lang=Francais):
        print(lang)
        ohce = OHCE(lang=lang)
        _lng = LangSelector(lang)

        self.assertEqual(lang.bonjour + " " + "YEH!" + " " + lang.au_revoir, ohce.traiter("!HEY"))
        self.assertEqual(lang.bonjour + " " + "YEY" + " " + lang.bien_dit + " " + lang.au_revoir, ohce.traiter("YEY"))
