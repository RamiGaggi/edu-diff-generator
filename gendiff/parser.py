"""Argument parser."""

import argparse


def create_parser():
    """Parse arguments from CLI.

    Returns:
        Namespace object with arguments.
    """
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', type=str, help='set format of output')
    return parser.parse_args()
