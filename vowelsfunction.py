def search4letters(phrase: str, letters: str='aeiou') -> set:
    """Returns  chosen letters  in chosen phrase.
    If no letters chosen, defaults to vowels"""
    return set(letters).intersection(set(phrase))
