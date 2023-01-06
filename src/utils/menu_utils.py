def do_choice_menu(menu):
    _choice = 0
    while not _choice:
        _in = input('Entrer un entier : ')
        try:
            _choice = int(_in)
            assert 0 < _choice <= len(menu)
        except ValueError:
            print("Ceci n'est pas un nombre...")
        except AssertionError:
            print(f"Cet entier n'est pas valide (doit être compris entre 1 et {len(menu)})")
            _choice = 0
    for i, elem in enumerate(menu.items()):
        k, v = elem
        if i + 1 == _choice:
            return k
