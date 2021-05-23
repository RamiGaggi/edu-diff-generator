"""Output format."""

from gendiff.diff_maker import get_chain, get_diff_operator, get_key, get_val


def form_string(item):
    """Form string .

    Args:
        item (list): Diff item.

    Raises:
        TypeError: If there is no such a difference.

    Returns:
        str: example: '+ timeout: 20'.
    """
    key = get_key(item)
    val = get_val(item)
    diff_operator = get_diff_operator(item)
    if val == 'PARENT':
        if diff_operator == '_':
            return '  {0}: '.format(key)
        if diff_operator == '-':
            return '- {0}: '.format(key)
        if diff_operator == '+':
            return '+ {0}: '.format(key)
    if diff_operator == '_':
        return '  {0}: {1}'.format(key, val)
    if diff_operator == '-':
        return '- {0}: {1}'.format(key, val)
    if diff_operator == '+':
        return '+ {0}: {1}'.format(key, val)
    raise TypeError


def form_stylish(diff):
    """Form JSON plain text.

    Args:
        diff (list): List with  diff operators:

    Returns:
        str: JSON plain text.
    """
    string = ['{\n']

    def inner(indent=2, chain=()):  # noqa: WPS430
        for el in diff:
            key = get_key(el)
            val = get_val(el)
            el_chain = get_chain(el)
            if val != 'PARENT' and el_chain == chain:
                string.append(indent * ' ' + form_string(el) + '\n')
            elif el_chain == chain:
                string.append(indent * ' ' + form_string(el) + '{\n')
                inner(indent + 4, chain + (key,))
                string.append(indent * ' ' + '  }')
                string.append('\n')
    inner()

    string.append('}')
    return ''.join(string)
