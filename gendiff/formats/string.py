"""Generate diff in string format."""


def gen_string(key, value, operator=' '):
    """Generate values for forming string.

    Args:
        key (str): key of attribute
        value (str/int): value of attribute
        operator (str, optional): '+', '-'. Defaults to ' '.

    Returns:
        tuple: Items for froming string, example: '  - timeout: 50'.
    """
    return ('  ' + operator, key + ':', str(value))
