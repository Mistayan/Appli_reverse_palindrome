import os
import unittest

from parameterized import parameterized

from src.messages import Francais, LangSelector, English
from utilities.OHCE_Builder import OHCEBuilder


class TestOHCE(unittest.TestCase):

    def test_01_bonjour(self):
        """ Le programme dit TOUJOURS bonjour, en fonction de l'heure et de la langue de l'utilisateur"""
        # ETANT DONNE OHCE en français, le matin
        ohce = OHCEBuilder().prends_comme_langue(Francais).a_heure_donnee(8).build()
        lang = LangSelector(Francais)

        # ALORS on dit bonjour
        self.assertEqual(lang.bonjour, ohce.bonjour)

    def test_02_au_revoir(self):
        """ Le programme dit TOUJOURS Au revoir, en fonction de l'heure et de la langue de l'utilisateur"""
        # ETANT DONNE OHCE en français
        ohce = OHCEBuilder().prends_comme_langue(Francais).a_heure_donnee(8).build()
        lang = LangSelector(Francais)

        # ALORS on dit Bonne journée
        self.assertEqual(ohce.au_revoir, lang.bonne_journee)

    def test_02_palindrome(self):
        """ Quand on saisit un palindrome, alors, on renvoie le palindrome, ET "Bien dit!"  """
        # Etant donné l'OHCE en français
        ohce = OHCEBuilder().prends_comme_langue(Francais).a_heure_donnee(8).build()
        lang = Francais

        # quand on saisit un palindrome,
        _in = "toot"
        val = ohce.traiter(_in)

        # Alors celui-ci est renvoyé, et bien dit est envoyé ensuite
        self.assertTrue(_in in val, "la chaine devrait être renvoyée en miroir")
        self.assertRegex(val, _in + "\n" + lang.bien_dit)

    def test_03_radar(self):
        """ Test que OHCE renvoi une chaine complète sur radar """
        # Etant donné l'OHCE
        ohce = OHCEBuilder().prends_comme_langue(Francais).a_heure_donnee(8).build()
        lang = ohce._lang

        # QUAND on rentre radar
        _in = "radar"

        # on nous dit bonjour, affiche radar, bien dit, puis dit au revoir
        self.assertEqual(lang.bonjour + "\n" + "radar" + "\n" + lang.bien_dit
                         + "\n" + lang.bonne_journee, ohce.traiter(_in))

    def test_03_1_Radar(self):
        """ Test que OHCE renvoi une chaine complète sur un palindrome non-strict( str.lower() ) """
        # THEORY
        ohce = OHCEBuilder().prends_comme_langue(Francais).a_heure_donnee(8).build()
        lang = ohce._lang

        _in = "Radar"
        self.assertEqual(lang.bonjour + "\n" + "radaR" + "\n" + lang.bien_dit
                         + "\n" + lang.bonne_journee, ohce.traiter(_in))

    def test_04_chaine_complete_non_palindrome(self):
        """ Test l'existence du message d'au revoir """
        # ETANT DONNE l'OHCE en langue française, le matin
        ohce = OHCEBuilder().prends_comme_langue(Francais).a_heure_donnee(8).build()
        lang = Francais

        # SI l'utilisateur rentre
        _in = "tEstS"

        # ALORS OHCE renvoi bonjour, le miroir, bonne journée
        self.assertEqual(lang.bonjour + "\n" + "StsEt" + "\n" + lang.bonne_journee, ohce.traiter(_in))

    def test_05_invalid_in(self):
        """ Test des entrées invalides pour s'assurer que OHCE fonctionnera comme attendu en cas d'imprévus """
        ohce = OHCEBuilder().prends_comme_langue(Francais).a_heure_donnee(8).build()

        self.assertRaises(ValueError, ohce.traiter, 42)
        self.assertRaises(ValueError, ohce.traiter, self)
        self.assertRaises(ValueError, ohce.traiter, 1.42)
        self.assertRaises(ValueError, ohce.traiter, os)

    def test_06_multilingual_english(self, lang=English):
        """ S'assure que si OHCE prends <English> en langue, il écrira en <English>"""
        ohce = OHCEBuilder().prends_comme_langue(lang).a_heure_donnee(8).build()
        self.assertEqual(lang.bonjour + "\n" + "YEH!" + "\n" + lang.bonne_journee, ohce.traiter("!HEY"))
        self.assertEqual(lang.bonjour + "\n" + "YEY" + "\n" + lang.bien_dit + "\n" + lang.bonne_journee,
                         ohce.traiter("YEY"))

    def test_07_multilingual_french(self, lang=Francais):
        """ S'assure que si OHCE prends <Francais> en langue, il écrira en <Francais>"""
        ohce = OHCEBuilder().prends_comme_langue(lang).a_heure_donnee(8).build()

        self.assertEqual(lang.bonjour + "\n" + "YEH!" + "\n" + lang.bonne_journee, ohce.traiter("!HEY"))
        self.assertEqual(lang.bonjour + "\n" + "YEY" + "\n" + lang.bien_dit + "\n" + lang.bonne_journee,
                         ohce.traiter("YEY"))

    @parameterized.expand([
        [0, Francais.late_nighter, Francais],
        [1, Francais.late_nighter, Francais],
        [6, Francais.bonjour, Francais],
        [8, Francais.bonjour, Francais],
        [12, Francais.bonjour, Francais],
        [16, Francais.bon_apres_midi, Francais],
        [20, Francais.bonsoir, Francais],
        [23, Francais.bonsoir, Francais],
        [0, English.late_nighter, English],
        [1, English.late_nighter, English],
        [6, English.bonjour, English],
        [8, English.bonjour, English],
        [12, English.bonjour, English],
        [16, English.bon_apres_midi, English],
        [20, English.bonsoir, English],
        [23, English.bonsoir, English],

    ])
    def test_08_bonjour_multiple_times_lang(self, _heure, _attendu, _lang):
        """ S'assure qu'en <LANGUE>, en fonction de l'<heure>, les phrases d'<au revoir> changent"""
        # ETANT DONNE OHCE en <LANGUE>, à <heure> variable,
        ohce = OHCEBuilder().prends_comme_langue(_lang).a_heure_donnee(_heure).build()
        # Assure que le résultat attendu soit le bon, en <LANGUE>
        self.assertEqual(_attendu, ohce.bonjour)
