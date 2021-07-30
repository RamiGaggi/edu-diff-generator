"""Test plain output format for generate diff."""

from gendiff.gendiff import generate_diff


def template(file1, file2, expect, style='plain'):
    """Template for all tests.

    Args:
        file1 (str): Path to file1.
        file2 (str): Path to file2.
        expect (str): Expect result.
        style (str): Output style
    """
    with open(expect) as file:
        expect_file = file.read()
    assert generate_diff(file1, file2, style) == expect_file


def test_plain_format():
    """Test 2 recursive json-yaml files for plain output."""
    file1 = 'tests/fixtures/plain_format/pack1/file1.json'
    file2 = 'tests/fixtures/plain_format/pack1/file2.yaml'
    expect = 'tests/fixtures/plain_format/pack1/expect.txt'
    template(file1, file2, expect, style='plain')


def test_plain_format2():
    """Test 2  json-yaml files for plain output."""
    file1 = 'tests/fixtures/plain_format/pack2/file1.json'
    file2 = 'tests/fixtures/plain_format/pack2/file2.yaml'
    expect = 'tests/fixtures/plain_format/pack2/expect.txt'
    template(file1, file2, expect, style='plain')
