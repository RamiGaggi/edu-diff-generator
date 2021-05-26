"""Output format."""

from gendiff.diff_maker import (
    get_chain,
    get_changed_item,
    get_diff_operator,
    get_diff_status,
    get_key,
    get_val,
)

PROHIBITIONS = ('true', 'false', 'null', None, '[complex value]')


def form_string(item, status, val1=None, val2=None):
    """Form string.

    Args:
        item (list): Diff item.
        status (str): Status of diff item.
        val1 (str/int, optional): Diff item value. Defaults to None.
        val2 (str/int, optional): Diff item value. Defaults to None.

    Returns:
        Tuple to form string.
    """
    prop = "'" + '.'.join(get_chain(item) + (get_key(item),)) + "'"
    value = '[complex value]' if val1 == 'PARENT' else val1
    value2 = '[complex value]' if val2 == 'PARENT' else val2
    if value not in PROHIBITIONS and not isinstance(value, int):
        value = "'" + value + "'"
    if value2 not in PROHIBITIONS and not isinstance(value2, int):
        value2 = "'" + value2 + "'"

    if status == 'ADDED':
        return ('Property', prop, 'was added with value:', str(value))
    if status == 'REMOVED':
        return ('Property', prop, 'was removed')
    if status == 'CHANGED':
        return ('Property', prop, 'was updated.', 'From', str(value), 'to', str(value2))  # noqa: E501


def form_plain(diff):
    """Form strings in plain format.

    Args:
        diff (list): diff list

    Returns:
        str: String in plain format.
    """
    result = []
    for el in diff:
        val = get_val(el)
        status = get_diff_status(el)
        operator = get_diff_operator(el)
        if status == 'REMOVED' and operator == '-':
            result.append(form_string(el, status))
        elif status == 'ADDED' and operator == '+':
            result.append(form_string(el, status, val))
        elif status == 'CHANGED' and operator == '-':
            val2 = get_val(get_changed_item(el, diff))
            result.append(form_string(el, status, val, val2))
    result.sort(key=lambda attr: attr[1])
    result_strings = [' '.join(string) for string in result]
    return '\n'.join(result_strings)
