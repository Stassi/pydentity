from typing import Callable, Type, TypeVar

T = TypeVar('T')


def identity(x: T) -> T:
    """
    Identity function that returns the input value unchanged.

    :param x: The input value of any type T.
    :return: The same unchanged input value.
    """
    return x


def create_identity(t: Type[T]) -> Callable[[T], T]:
    """
    Creates and returns a type-specific identity function for the given type.

    :param t: The type for which the identity function should be created.
    :return: The type-specific identity function.
    """

    def typed_identity(x: t) -> t:
        """
        The type-specific identity function that returns its input of the specified type unchanged.

        :param x: The input value of the specified type.
        :return: The input value unchanged.
        """
        if not isinstance(x, t):
            raise TypeError(f'Expected value of type "{t.__name__}", got "{type(x).__name__}"')
        return x

    return typed_identity
