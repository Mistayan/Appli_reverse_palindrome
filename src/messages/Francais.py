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
    ohce_in = "Entrez une chaine de caractères"
    entier_in = "Entrez un Nombre"
    str_in = "Entrez un mot"
    not_str = "Ceci n'est pas une chaine de caractères"
    not_int = "Ceci n'est pas un nombre, ou il est invalide"
    int_invalid = "Cet entier n'est pas valide (doit être compris entre 1 et {})"
    # MENU
    go = "Lancer le programme"
    explorer = "explorer les methodes publiques du programme"
    explorer_module = " Choisissez quelle fonctionnalité explorer :"
    options = "changer de langue"
    quitter = "quitter"
    retour = "Retour"

    def __str__(self):
        return "Francais"
