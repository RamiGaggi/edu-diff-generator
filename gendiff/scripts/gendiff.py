#!/usr/bin/env python

"""Script to start the difference checker."""
import json

from gendiff.formats.string import gen_string
from gendiff.parser import create_parser


def generate_diff(path_to_file1, path_to_file2):  # noqa: WPS210, WPS231
    """Generate diff between two files.

    Args:
        path_to_file1 (str): Path to first file.
        path_to_file2 (str): Path to second file

    Returns:
        str: [description]
    """
    with open(path_to_file1) as file1, open(path_to_file2) as file2:  # noqa: WPS316, E501
        json_file1 = json.load(file1)
        json_file2 = json.load(file2)

    result_diff_list = []
    for key, value in {**json_file1, **json_file2}.items():
        if key in json_file1 and key in json_file2:
            if json_file1[key] == value:
                result_diff_list += [gen_string(key, value)]
            else:
                result_diff_list += [gen_string(key, json_file1.get(key), '-')]
                result_diff_list += [gen_string(key, value, '+')]
            continue
        elif key in json_file1:
            result_diff_list += [gen_string(key, json_file1.get(key), '-')]
        else:
            result_diff_list += [gen_string(key, value, '+')]
    # Sorting by attr, example: ('-', 'timeout:', 50)
    result_diff_list.sort(key=lambda attr: attr[1])
    result_diff = [' '.join(item) for item in result_diff_list]

    return '{\n' + '\n'.join(result_diff) + '\n}'


def main():
    """Run the programm."""
    args = create_parser()
    file1 = args.first_file
    file2 = args.second_file
    print(generate_diff(file1, file2))


if __name__ == '__main__':
    main()
