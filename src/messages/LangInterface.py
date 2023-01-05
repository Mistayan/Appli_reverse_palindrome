from abc import ABC


class LangInterface(ABC):
    """
    Une interface ne peut pas être instanciée --> ABC
    Elle permet:
     - l'uniformisation des sous-classes
     - qu'une classe enfant soit toujours considérée <LangInterface>, quelque soit son nom.
    """
    bonjour: str
    bonsoir: str
    bienvenu: str
    au_revoir: str
    bonne_soiree: str
    bien_dit: str
    OHCE_INPUT: str
    rien_fourni: str
    impossible_reverse: str
