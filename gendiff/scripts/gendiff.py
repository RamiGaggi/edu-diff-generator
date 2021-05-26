#!/usr/bin/env python

"""Script to start the difference checker."""

from gendiff.gendiff import generate_diff
from gendiff.parser import create_arg_parser


def main():
    """Run the programm."""
    args = create_arg_parser()
    file1 = args.first_file
    file2 = args.second_file
    output_format = args.format
    print(generate_diff(file1, file2, output_format))


if __name__ == '__main__':
    main()
