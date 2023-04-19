from typing import Union


def parse_string(value: str) -> Union[bool, float, int, str, None]:
    """
    Parse a string and return the appropriate type.

    :param value: The input as a string.
    :return: The input converted to its corresponding type.
    """
    try:
        return int(value)
    except ValueError:
        pass

    try:
        return float(value)
    except ValueError:
        pass

    value_lower = value.lower()
    if value_lower == "true":
        return True
    elif value_lower == "false":
        return False
    elif value_lower == "none":
        return None
    else:
        return value.strip('"')
