import json
import pytest
from gendiff import generate_diff


def read_file(path):
    with open(path, 'r') as file:
        return file.read().strip()


def test_flat_json_diff():
    file1 = 'tests/fixtures/file1.json'
    file2 = 'tests/fixtures/file2.json'
    expected = read_file('tests/fixtures/expected_flat.txt')

    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        data1 = json.load(f1)
        data2 = json.load(f2)

    result = generate_diff(data1, data2)
    assert result == expected


def test_flat_yaml_diff():
    file1 = 'tests/fixtures/file1.yml'
    file2 = 'tests/fixtures/file2.yml'
    expected = read_file('tests/fixtures/expected_flat.txt')

    result = generate_diff(file1, file2)
    assert result == expected


def test_generate_diff_with_empty_files():
    result = generate_diff({}, {})
    assert result == "{}"


def test_parsers():
    from gendiff.parsers import parse_data, get_format

    # Test JSON parser
    json_data = '{"key": "value"}'
    assert parse_data(json_data, 'json') == {"key": "value"}

    # Test YAML parser
    yaml_data = 'key: value'
    assert parse_data(yaml_data, 'yaml') == {"key": "value"}

    # Test format detection
    assert get_format('file.json') == 'json'
    assert get_format('file.yaml') == 'yaml'
    assert get_format('file.yml') == 'yaml'

    # Test unsupported format
    with pytest.raises(ValueError):
        get_format('file.txt')


def test_yaml_vs_yaml():
    """Тест сравнения двух YAML файлов с разными данными"""
    yaml_file1 = 'tests/fixtures/file1.yml'
    yaml_file2 = 'tests/fixtures/file2.yml'
    expected = read_file('tests/fixtures/expected_flat.txt')

    result = generate_diff(yaml_file1, yaml_file2)
    assert result == expected


def test_mixed_formats_same_data():
    """Тест сравнения одинаковых данных в разных форматах"""
    json_file = 'tests/fixtures/file1.json'
    yaml_file = 'tests/fixtures/file1_identical.yml'

    result = generate_diff(json_file, yaml_file)
    # Ожидаем все ключи без изменений (без - и +)
    expected_lines = [
        "{",
        "    follow: false",
        "    host: hexlet.io",
        "    proxy: 123.234.53.22",
        "    timeout: 50",
        "}"
    ]
    expected = "\n".join(expected_lines)
    assert result == expected
