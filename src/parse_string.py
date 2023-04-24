from ast import literal_eval
from types import EllipsisType


def parse_string(value: str) -> bool | bytes | dict | EllipsisType | float | int | list | set | str | tuple | None:
    """
    Parse a string and return the appropriate type.

    :param value: The input as a string.
    :return: The input converted to its corresponding type.
    """
    return literal_eval(value)
