"""[summary]."""
import argparse
import json


def create_arg_parser():
    """Parse arguments from CLI.

    Returns:
        Namespace object with arguments.
    """
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', type=str, help='set format of output')
    return parser.parse_args()


def parse_file(path_to_file):
    """[summary].

    Args:
        path_to_file (str): Path to file.

    Returns:
        dictionary: JSON, YAML
    """
    if path_to_file.endswith('.json'):
        with open(path_to_file) as file:
            result = json.load(file)
    return result
