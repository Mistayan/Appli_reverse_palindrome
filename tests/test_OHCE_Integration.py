import unittest

from messages import English, Francais
from models import OHCE
from models.Clock import Clock


class OHCEIntegrationTests(unittest.TestCase):

    def test_scenarii_palindrome_soir_en(self):
        """
        Etant donné
        """

        # ETANT DONNE que nous sommes le soir
        soir = Clock().set_time(21).time

        # ET que l'utilisateur parle anglais
        lang = English

        # QUAND il entre un palindrome
        resultat = OHCE(lang=lang, time=soir).traiter("YEY")

        # ALORS il est salué
        self.assertRegex(resultat, r"^{}".format(lang.bonsoir), "OHCE doit dire bonjour")

        # PUIS son palindrome est imprimé
        self.assertRegex(resultat, r"^{} {}".format(lang.bonsoir, "YEY"))

        # PUIS il est félicité
        self.assertRegex(resultat, r"{} {}".format("YEY", lang.bien_dit))

        # PUIS on lui dit bonne nuit
        self.assertRegex(resultat, r"{} {}".format(lang.bien_dit, lang.bonne_nuit))

    def test_scenarii_non_palindrome_matin_fr(self):
        """
        Etant donné
        """

        # ETANT DONNE que nous sommes le soir
        soir = Clock().set_time(9).time

        # ET que l'utilisateur parle anglais
        lang = Francais

        # QUAND il entre un palindrome
        resultat = OHCE(lang=lang, time=soir).traiter("HEY")

        # ALORS il est salué
        self.assertRegex(resultat, r"^{}".format(lang.bonjour), "OHCE doit dire bonjour")

        # PUIS son palindrome est imprimé
        self.assertRegex(resultat, r"^{} {}".format(lang.bonjour, "YEH"))

        # PUIS on lui souhaite une bonne journée
        self.assertRegex(resultat, r"{} {}".format("YEH", lang.bonne_journee))
