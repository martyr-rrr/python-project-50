import json
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


def test_generate_diff_with_empty_files():
    result = generate_diff({}, {})
    assert result == "{}"
