from abc import ABC, ABCMeta


class LangInterface(ABC, metaclass=ABCMeta):
    """
    Une interface ne peut pas être instanciée --> ABC
    Elle permet:
     - l'uniformisation des sous-classes
     - qu'une classe enfant soit toujours considérée <LangInterface>, quelque soit son nom.
    """
    # BONJOUR
    bonjour: str
    bonsoir: str
    late_nighter: str

    # AU REVOIR
    de_bon_matin: str
    au_revoir: str
    bonne_journee: str
    bonne_soiree: str
    bonne_nuit: str
    vas_te_coucher: str
    bon_apres_midi: str

    # OHCE
    bien_dit: str
    OHCE_INPUT: str
    rien_fourni: str
    impossible_reverse: str
    lang_select: str
    ohce_in: str
    entier_in: str
    str_in: str
    not_str: str
    not_int: str
    int_invalid: str

    # MENU
    go: str
    explorer: str
    explorer_module: str
    options: str
    quitter: str
    retour: str
