"""Tests."""

from gendiff.gendiff import generate_diff


def template(file1, file2, expect):
    """Template for all tests.

    Args:
        file1 (str): Path to file1.
        file2 (str): Path to file2.
        expect (str): Expect result.
    """
    with open(expect) as file:
        expect = file.read()
    assert generate_diff(file1, file2) == expect


def test_flat_json1():
    """Test 2  empty json files."""
    file1 = 'fixtures/flat_json/pack2/file1.json'
    file2 = 'fixtures/flat_json/pack2/file2.json'
    expect = 'fixtures/flat_json/pack2/expect.txt'
    template(file1, file2, expect)


def test_flat_json2():
    """Test 2 flat json files."""
    file1 = 'fixtures/flat_json/pack1/file1.json'
    file2 = 'fixtures/flat_json/pack1/file2.json'
    expect = 'fixtures/flat_json/pack1/expect.txt'
    template(file1, file2, expect)
