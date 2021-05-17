"""Argument parser."""

import argparse


def create_parser():
    """Parse arguments from CLI.

    Returns:
        Namespace object with arguments.
    """
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    return parser.parse_args()
