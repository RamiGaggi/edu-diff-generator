"""Output format."""

import json

from gendiff.diff_maker import (
    get_chain,
    get_diff_operator,
    get_diff_status,
    get_key,
    get_val,
)


def form_key(item):
    """Form key with diff operator.

    Args:
        item (list): Diff item.

    Returns:
        str: Key with diff operator.
    """
    key = get_key(item)
    diff_operator = get_diff_operator(item)
    diff_status = get_diff_status(item)
    if diff_operator == '-' and diff_status in {'REMOVED', 'CHANGED'}:
        return '- ' + key
    if diff_operator == '+' and diff_status in {'CHANGED', 'ADDED'}:
        return '+ ' + key
    return key


def form_json(diff):
    """Form json diff.

    Args:
        diff (list): Diff list.

    Returns:
        str: Diff json.
    """
    result = {}

    def inner(parent=result, chain=()):  # noqa: WPS430
        for el in diff:
            val = get_val(el)
            el_chain = get_chain(el)
            key = get_key(el)
            if val != 'PARENT' and el_chain == chain:
                parent[form_key(el)] = val
            elif el_chain == chain:
                parent[form_key(el)] = inner({}, chain + (key,))
        return parent
    inner()

    return json.dumps(result, indent=4)
