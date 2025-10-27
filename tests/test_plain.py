from gendiff import generate_diff


def read_file(path):
    with open(path, 'r') as f:
        return f.read()


def test_plain_format():
    file1 = 'tests/fixtures/nested/file1.json'
    file2 = 'tests/fixtures/nested/file2.json'
    result = generate_diff(file1, file2, 'plain')
    expected_lines = [
        "Property 'common.follow' was added with value: false",
        "Property 'common.setting2' was removed",
        "Property 'common.setting3' was updated. From true to null",
        "Property 'common.setting4' was added with value: 'blah blah'",
        "Property 'common.setting5' was added with value: [complex value]",
        "Property 'common.setting6.doge.wow' was updated. From '' to 'so much'",  # noqa: E501
        "Property 'common.setting6.ops' was added with value: 'vops'",
        "Property 'group1.baz' was updated. From 'bas' to 'bars'",
        "Property 'group1.nest' was updated. From [complex value] to 'str'",
        "Property 'group2' was removed",
        "Property 'group3' was added with value: [complex value]"
    ]
    for line in expected_lines:
        assert line in result


def test_plain_format_with_flat_files():
    file1 = 'tests/fixtures/file1.json'
    file2 = 'tests/fixtures/file2.json'
    result = generate_diff(file1, file2, 'plain')
    expected_lines = [
        "Property 'follow' was removed",
        "Property 'proxy' was removed",
        "Property 'timeout' was updated. From 50 to 20",
        "Property 'verbose' was added with value: true"
    ]
    for line in expected_lines:
        assert line in result


def test_plain_format_with_yaml():
    file1 = 'tests/fixtures/nested/file1.yml'
    file2 = 'tests/fixtures/nested/file2.yml'
    result = generate_diff(file1, file2, 'plain')
    assert "Property 'common.follow' was added with value: false" in result
    assert "Property 'common.setting2' was removed" in result


def test_exact_plain_format():
    file1 = 'tests/fixtures/nested/file1.json'
    file2 = 'tests/fixtures/nested/file2.json'
    expected = read_file('tests/fixtures/nested/expected_plain.txt')
    result = generate_diff(file1, file2, 'plain')
    expected_lines = expected.strip().split('\n')
    result_lines = result.strip().split('\n')
    for i, (exp, res) in enumerate(zip(expected_lines, result_lines)):
        error_msg = f"Line {i + 1} mismatch:\nExpected: {exp}\nActual: {res}"
        assert exp == res, error_msg
    diff_lines_msg = "Different number of lines"
    assert len(expected_lines) == len(result_lines), diff_lines_msg
