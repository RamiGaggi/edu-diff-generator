"""Tools for making compare between two configurations."""
from copy import deepcopy


def flat_dict(source):
    """Flat dictinoary to the list of uniq items .

    Args:
        source (dict): Dictionary.

    Returns:
        list: List of uniq items, example.
        Example of item:
        ['type', 'json', ()], where is:
        [0]: key, [1]: value, [2]: parents chain.
    """
    result = []

    def inner(children, chain=()):  # noqa: WPS430
        for key, value in children.items():
            if isinstance(value, dict):
                result.append([key, 'PARENT', chain])
                inner(value, chain + (key,))
            else:
                if value is None:
                    value = 'null'
                if value is True:
                    value = 'true'
                if value is False:
                    value = 'false'
                result.append([key, value, chain])

    inner(source)
    return result


def get_val(item):
    """Get item value of flat dictionary.

    Args:
        item (list): list of uniq items

    Returns:
        Any item value.
    """
    return item[1]


def get_key(item):
    """Get item key of flat dictionary.

    Args:
        item (list): list of uniq items

    Returns:
        str: Item key.
    """
    return item[0]


def get_chain(item):
    """Get item parent chain of flat dictionary.

    Args:
        item (list): list of uniq items

    Returns:
        tuple: Parents chain.
    """
    return item[2]


def get_diff_operator(item):
    """Get item diff operator of flat dictionary.

    Args:
        item (list): list of uniq items

    Returns:
        str: Item key.
    """
    return item[3]


def normalized(flat_diff):
    """Omit duplicate diff operators for child elements.

    Args:
        flat_diff (list): list of uniq items

    Returns:
        list: New normalazied diff list.
    """
    flat_diff_copy = deepcopy(flat_diff)
    for el in flat_diff:
        if get_val(el) == 'PARENT' and get_diff_operator(el) in {'-', '+'}:
            chain = get_chain(el) + (get_key(el), )
            for ind, child in enumerate(flat_diff):
                if chain == get_chain(child):
                    flat_diff_copy[ind][3] = '_'
    return flat_diff_copy


def create_diff(flat_dict1, flat_dict2):
    """Compare two flat-dict structures.

    Args:
        flat_dict1 (list): List of uniq items.
        flat_dict2 (list): List of uniq items.

    Returns:
        list: List with  diff operators:
        ['follow', 'false', (), '-']
        [0]: key, [1]: value, [2]: parents chain,
        [3]: diff operator -('-' - removed, '+' - addeed, '_' - without changes)
    """
    result = []

    for el in flat_dict1:  # noqa: WPS426
        key = get_key(el)
        val = get_val(el)
        if el in flat_dict2:
            result.append(el + ['_'])
        elif [key, val] in map(lambda item: [item[0], item[1]], flat_dict2):
            result.append(el + ['-'])
        else:
            result.append(el + ['-'])

    for el in flat_dict2:
        if el in flat_dict1:
            continue
        else:
            result.append(el + ['+'])
    result.sort(key=lambda item: item[0])
    return normalized(result)
