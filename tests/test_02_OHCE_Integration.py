import unittest
from functools import partial

from src.messages import English, Francais
from src.models import OHCE
from tests.utilities.OHCE_Builder import OHCEBuilder
from utilities.ClockMock import ClockMock


class OHCEIntegrationTests(unittest.TestCase):

    def test_scenarii_palindrome_soir_en(self):
        """
        Scenario de test d'un palindrome, le soir, en English
        """

        # ETANT DONNE que nous sommes le soir
        # ET que l'utilisateur parle anglais
        lang = English
        ohce = OHCEBuilder().prends_comme_langue(lang=lang).a_heure_donnee(21).build()

        # QUAND il entre un palindrome
        resultat = ohce.traiter("YEY")

        # ALORS il est salué
        self.assertRegex(resultat, r"^{}".format(lang.bonsoir), "OHCE doit dire bonsoir")

        # PUIS son palindrome est imprimé
        self.assertRegex(resultat, r"^{}\n{}\n".format(lang.bonsoir, "YEY"),
                         "Le palindrome doit se trouver après bonsoir")

        # PUIS il est félicité
        self.assertRegex(resultat, r"\n{}\n{}\n".format("YEY", lang.bien_dit),
                         "Les félicitations pour un palindrome doit se trouver après le mot")

        # PUIS on lui dit bonne nuit
        self.assertRegex(resultat, r"\n{}\n{}$".format(lang.bien_dit, lang.bonne_nuit),
                         "le message d'au revoir doit se trouver après bien_dit")

    def test_scenarii_non_palindrome_matin_fr(self):
        """
        Scenario de test d'un non-palindrome, le matin, en Francais
        """
        # ETANT DONNE que nous sommes le soir
        soir = partial(ClockMock, 9)

        # ET que l'utilisateur parle anglais
        lang = Francais()

        # QUAND il entre un non-palindrome
        resultat = OHCE(lang=lang, clock=soir).traiter("HEY")

        # ALORS il est salué
        self.assertRegex(resultat, r"^{}\n".format(lang.bonjour), "OHCE doit dire bonjour en premier")

        # PUIS son miroir est imprimé
        self.assertRegex(resultat, r"^{}\n{}\n".format(lang.bonjour, "YEH"),
                         "Le miroir du mot doit se trouver après bonjour")

        # PUIS on lui souhaite une bonne journée
        self.assertRegex(resultat, r"\n{}\n{}$".format("YEH", lang.bonne_journee),
                         "Le message d'au_revoir doit se trouver après le mot en miroir et à la fin")
