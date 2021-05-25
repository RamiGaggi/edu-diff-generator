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


def get_diff_status(item):
    """Get item diff status of flat dictionary.

    Args:
        item (list): list of uniq items

    Returns:
        str: Status: 'ADDED', 'REMOVED', 'CHANGED', 'UNCHANGED'.
    """
    return item[4]


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
        [3]: diff operator
        [4]: diff status - ('-' - removed, '+' - addeed, '_' - without changes)
    """
    result = []

    for el in flat_dict1:  # noqa: WPS426
        key = get_key(el)
        chain = get_chain(el)
        if el in flat_dict2:
            result.append(el + ['_'] + ['UNCHANGED'])
        elif [key, chain] in map(lambda item: [item[0], item[2]], flat_dict2):
            result.append(el + ['-'] + ['CHANGED'])
        else:
            result.append(el + ['-'] + ['REMOVED'])

    for el2 in flat_dict2:
        key2 = get_key(el2)
        chain2 = get_chain(el2)
        if el2 in flat_dict1:
            continue
        elif [key2, chain2] in map(lambda item: [item[0], item[2]], flat_dict1):
            result.append(el2 + ['+'] + ['CHANGED'])
        else:
            result.append(el2 + ['+'] + ['ADDED'])
    result.sort(key=lambda item: item[0])
    return normalized(result)


def get_changed_item(source_item, diff):
    """Find a source item with changed value.

    Args:
        source_item (list): Diff item.
        diff (list): List with a difference between two files.

    Returns:
        list: Item with changed value.
    """
    key = get_key(source_item)
    chain = get_chain(source_item)
    result = filter(lambda el: (el[0] == key and el[2] == chain and el[3] == '+'), diff)  # noqa: E501
    return list(result)[0]
