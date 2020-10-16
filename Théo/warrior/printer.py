def ask(message: str, accepted: list):
    choice = None
    while choice not in accepted:
        choice = input(message)
        if choice.isdigit():
            try:
                choice = int(choice)
            except typeError:
                choice = choice
        else:
            choice = choice.lower()

    return choice
