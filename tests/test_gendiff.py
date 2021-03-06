"""Tests."""

import json

import pytest
from gendiff.gendiff import generate_diff
from gendiff.parser import parse_file


def template(file1, file2, expect, style='stylish'):
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


def test_flat_json1():
    """Test 2  empty json files."""
    file1 = 'tests/fixtures/flat_json/pack2/file1.json'
    file2 = 'tests/fixtures/flat_json/pack2/file2.json'
    expect = 'tests/fixtures/flat_json/pack2/expect.txt'
    template(file1, file2, expect)


def test_flat_json2():
    """Test 2 flat json files."""
    file1 = 'tests/fixtures/flat_json/pack1/file1.json'
    file2 = 'tests/fixtures/flat_json/pack1/file2.json'
    expect = 'tests/fixtures/flat_json/pack1/expect.txt'
    template(file1, file2, expect)


def test_flat_yaml1():
    """Test 2 flat yaml files."""
    file1 = 'tests/fixtures/flat_yaml/pack1/file1.yaml'
    file2 = 'tests/fixtures/flat_yaml/pack1/file2.yml'
    expect = 'tests/fixtures/flat_yaml/pack1/expect.txt'
    template(file1, file2, expect)


def test_flat_yaml2():
    """Test 2 flat yaml files."""
    file1 = 'tests/fixtures/flat_yaml/pack2/file1.yaml'
    file2 = 'tests/fixtures/flat_yaml/pack2/file2.yml'
    expect = 'tests/fixtures/flat_yaml/pack2/expect.txt'
    template(file1, file2, expect)


def test_flat_yaml_json():
    """Test 2 flat json-yaml files."""
    file1 = 'tests/fixtures/flat_yaml/pack1/file1.yaml'
    file2 = 'tests/fixtures/flat_json/pack1/file2.json'
    expect = 'tests/fixtures/flat_yaml/pack1/expect.txt'
    template(file1, file2, expect)


def test_recursive():
    """Test 2 recursive json-yaml files."""
    file1 = 'tests/fixtures/recursive/file1.json'
    file2 = 'tests/fixtures/recursive/file2.yaml'
    expect = 'tests/fixtures/recursive/expect.txt'
    template(file1, file2, expect)


def test_json_format():
    """Test 2  json-yaml files for plain output."""
    file1 = 'tests/fixtures/json_format/file1.json'
    file2 = 'tests/fixtures/json_format/file2.yaml'
    expect = 'tests/fixtures/json_format/expect.json'
    assert parse_file(expect) == json.loads(
        generate_diff(file1, file2, style='json'),
    )


def test_unsupported_format():
    """Test unsupported type files."""
    file1 = 'tests/fixtures/unsupported_type/file1.xml'
    file2 = 'tests/fixtures/unsupported_type/file2.xml'
    with pytest.raises(TypeError):
        generate_diff(file1, file2)
