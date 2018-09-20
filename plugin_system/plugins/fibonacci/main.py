from .fib_calc import fib


def main(*args, **kwargs):
    return fib(kwargs['n'])
