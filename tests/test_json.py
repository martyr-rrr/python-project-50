import json
from gendiff.core import generate_diff


def test_json_format():
    file1 = 'tests/fixtures/nested/file1.json'
    file2 = 'tests/fixtures/nested/file2.json'
    result = generate_diff(file1, file2, 'json')
    try:
        parsed = json.loads(result)
        assert isinstance(parsed, list)
        keys = [node['key'] for node in parsed]
        assert 'common' in keys
        assert 'group1' in keys
        assert 'group2' in keys
        assert 'group3' in keys
    except json.JSONDecodeError:
        assert False, "Result is not valid JSON"


def test_json_format_with_flat_files():
    file1 = 'tests/fixtures/file1.json'
    file2 = 'tests/fixtures/file2.json'
    result = generate_diff(file1, file2, 'json')
    try:
        parsed = json.loads(result)
        assert isinstance(parsed, list)
    except json.JSONDecodeError:
        assert False, "Result is not valid JSON"


def test_json_format_with_yaml():
    file1 = 'tests/fixtures/nested/file1.yml'
    file2 = 'tests/fixtures/nested/file2.yml'
    result = generate_diff(file1, file2, 'json')
    try:
        parsed = json.loads(result)
        assert isinstance(parsed, list)
    except json.JSONDecodeError:
        assert False, "Result is not valid JSON"


def test_json_format_structure():
    file1 = 'tests/fixtures/nested/file1.json'
    file2 = 'tests/fixtures/nested/file2.json'
    result = generate_diff(file1, file2, 'json')
    parsed = json.loads(result)
    common_node = next(node for node in parsed if node['key'] == 'common')
    assert common_node['type'] == 'nested'
    assert isinstance(common_node['children'], list)
    added_nodes = [node for node in common_node['children'] if node['type'] == 'added']  # noqa: E501
    removed_nodes = [node for node in common_node['children'] if node['type'] == 'removed']  # noqa: E501
    assert len(added_nodes) > 0
    assert len(removed_nodes) > 0
