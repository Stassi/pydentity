from typing import TypeVar

T = TypeVar('T')


def identity(x: T) -> T:
    """
    Identity function that returns the input value unchanged.

    :param x: The input value of any type T.
    :return: The same unchanged input value.
    """
    return x
