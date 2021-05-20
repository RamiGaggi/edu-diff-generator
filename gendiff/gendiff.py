"""Generates diff for two files."""

from gendiff.parser import parse_file


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


def generate_diff(path_to_file1, path_to_file2):  # noqa: WPS210, WPS231
    """Generate diff between two files.

    Args:
        path_to_file1 (str): Path to first file.
        path_to_file2 (str): Path to second file

    Returns:
        str: [description]
    """
    json_file1 = parse_file(path_to_file1)
    json_file2 = parse_file(path_to_file2)
    result_diff_list = []
    for key, value in {**json_file1, **json_file2}.items():
        if key in json_file1 and key in json_file2:
            if json_file1[key] == value:
                result_diff_list.append(gen_string(key, value))
            else:
                result_diff_list.append(gen_string(key, json_file1.get(key), '-'))  # noqa: E501
                result_diff_list.append(gen_string(key, value, '+'))
            continue
        elif key in json_file1:
            result_diff_list.append(gen_string(key, json_file1.get(key), '-'))
        else:
            result_diff_list.append(gen_string(key, value, '+'))
    # Sorting by attr[1], example: ('-', 'timeout:', 50)
    result_diff_list.sort(key=lambda attr: attr[1])
    result_diff = [' '.join(item) for item in result_diff_list]

    return '{\n' + '\n'.join(result_diff) + '\n}' if result_diff else repr({})
