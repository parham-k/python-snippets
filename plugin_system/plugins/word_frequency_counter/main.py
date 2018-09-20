from .counter import get_word_frequencies


def main(*args, **kwargs):
    return get_word_frequencies(kwargs['words'])
