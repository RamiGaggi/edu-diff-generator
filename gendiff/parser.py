"""Parse files and CLI arguments."""
import argparse
import json

import yaml


def create_arg_parser():
    """Parse arguments from CLI.

    Returns:
        Namespace object with arguments.
    """
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument(
        '-f',
        '--format',
        type=str,
        help='set format of output',
        default='stylish',
    )
    return parser.parse_args()


def parse_file(path_to_file):
    """Parse JSON/YAML files.

    Args:
        path_to_file (str): Path to file.

    Raises:
        TypeError: Raise if the file is not JSON/YAML format.

    Returns:
        dictionary: JSON, YAML
    """
    if path_to_file.endswith('.json'):
        with open(path_to_file) as json_file:
            return json.load(json_file)
    if path_to_file.endswith('.yaml') or path_to_file.endswith('.yml'):
        with open(path_to_file) as yaml_file:
            return yaml.safe_load(yaml_file)
    raise TypeError('Unsupported file type!')
