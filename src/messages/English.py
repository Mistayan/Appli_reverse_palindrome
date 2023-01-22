from src.messages.LangInterface import LangInterface


class English(LangInterface):
    # Entry
    bonjour = "Hello"
    bonsoir = "Good evening"
    late_nighter = "Hard coder !"

    # Exit
    au_revoir = "Goodbye"
    bonne_soiree = "Good night"
    bon_apres_midi = "Good Afternoon"
    de_bon_matin = "Early practice"
    bonne_journee = "Have a nice day"
    bonne_nuit = "Good night"
    vas_te_coucher = "Go to bed !"

    # OHCE
    bien_dit = "Well said!"
    OHCE_INPUT = "Please insert a word"
    rien_fourni = "Nothing has been provided"
    impossible_reverse = "Cannot reverse this"
    lang_select = "Language selected : English"
    ohce_in = "Enter  a String"
    entier_in = "Input a number"
    str_in = "Input a word"
    not_str = "not a word"
    not_int = "not a number"
    int_invalid = "Invalid number (expected between 1 and {})"

    # MENU
    go = "Start the program"
    explorer = "Explore program's public methods"
    explorer_module = "Choose one of api public methods to explore"
    options = "Change language"
    quitter = "Exit"
    retour = "Back"
    # TEST
    test = ""

    def __str__(self):
        return "English"
