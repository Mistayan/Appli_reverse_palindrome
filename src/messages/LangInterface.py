import locale

from src.messages.English import English
from src.messages.Francais import Francais


class LangInterface:
    lang, formatting = locale.getlocale()
    match lang:
        case "English_United States":
            msgs = English()
        case "English_Great Britain":
            msgs = English()
        case _:
            msgs = Francais()
