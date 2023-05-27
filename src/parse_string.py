from ast import literal_eval


def parse_string(value: str) -> bool | bytes | dict | type(Ellipsis) | float | int | list | set | str | tuple | None:
    """
    Parse a string and return the appropriate type.

    :param value: The input as a string.
    :return: The input converted to its corresponding type.
    """
    return literal_eval(value)
