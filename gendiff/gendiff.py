"""Generates diff between two files."""

from gendiff.diff_maker import create_diff, flat_dict
from gendiff.formats.json import form_json
from gendiff.formats.plain import form_plain
from gendiff.formats.stylish import form_stylish
from gendiff.parser import parse_file


# noqa: WPS210, WPS231
def generate_diff(path_to_file1, path_to_file2, style='stylish'):  # noqa: C901
    """Generate diff between two files.

    Args:
        path_to_file1 (str): Path to first file.
        path_to_file2 (str): Path to second file
        style (str): Show the difference in a certain style.

    Raises:
        NameError: [description]

    Returns:
        str: [description]
    """
    file1 = parse_file(path_to_file1)
    file2 = parse_file(path_to_file2)
    if not file1 and not file2:
        return repr({})
    if style in {'stylish', 'plain'}:
        diff = create_diff(flat_dict(file1), flat_dict(file2))
    elif style == 'json':
        diff = create_diff(flat_dict(file1, convert=False), flat_dict(file2, convert=False))  # noqa: E501
    else:
        raise NameError('There is no such a format!')

    if style == 'stylish':
        return form_stylish(diff)
    if style == 'plain':
        return form_plain(diff)
    if style == 'json':
        return form_json(diff)
