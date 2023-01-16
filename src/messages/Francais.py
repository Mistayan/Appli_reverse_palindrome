from src.messages.LangInterface import LangInterface


class Francais(LangInterface):
    # BONJOUR
    bonjour = "Bonjour"
    de_bon_matin = "Le monde appartient à ceux qui se lèvent tôt"
    bonsoir = "Bonsoir"
    late_nighter = "Ca code dur !"

    # AU REVOIR
    au_revoir = "Au revoir"
    bonne_soiree = "Bonne soirée"
    bon_apres_midi = "Bon après-midi"
    bonne_journee = "Bonne journée"
    vas_te_coucher = "Vas te coucher"
    bonne_nuit = "Bonne nuit !"

    # OHCE
    bien_dit = "Bien dit!"
    OHCE_INPUT = "Entrez un mot"
    rien_fourni = "Rien n'a été fourni"
    impossible_reverse = "Impossible de permuter cela"
    lang_select = "Langue choisie : Francais"

    def __str__(self):
        return "Francais"
