#!/usr/bin/env python

"""Script to start the difference checker."""

from gendiff.parser import create_parser


def main():
    """Run the programm."""
    print(create_parser())


if __name__ == '__main__':
    main()
