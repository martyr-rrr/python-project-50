from gendiff import generate_diff


def read_file(path):
    with open(path, 'r') as file:
        return file.read()


def test_nested_json_diff():
    file1 = 'tests/fixtures/nested/file1.json'
    file2 = 'tests/fixtures/nested/file2.json'

    result = generate_diff(file1, file2)

    # Проверим что результат содержит ожидаемые ключевые элементы
    assert 'common:' in result
    assert '+ follow: false' in result
    assert '- setting2: 200' in result
    assert '- setting3: true' in result
    assert '+ setting3: null' in result
    assert 'doge:' in result
    assert '- wow:' in result or '- wow: ' in result
    assert '+ wow: so much' in result


def test_nested_yaml_diff():
    file1 = 'tests/fixtures/nested/file1.yml'
    file2 = 'tests/fixtures/nested/file2.yml'

    result = generate_diff(file1, file2)

    # Должен быть такой же результат как для JSON
    assert 'common:' in result
    assert '+ follow: false' in result
    assert '- setting2: 200' in result


def test_format_selection():
    file1 = 'tests/fixtures/nested/file1.json'
    file2 = 'tests/fixtures/nested/file2.json'

    # Должен работать stylish по умолчанию
    result_default = generate_diff(file1, file2)
    result_stylish = generate_diff(file1, file2, 'stylish')

    assert result_default == result_stylish


def test_flat_files_still_work():
    """Проверим что плоские файлы все еще работают"""
    file1 = 'tests/fixtures/file1.json'
    file2 = 'tests/fixtures/file2.json'

    result = generate_diff(file1, file2)
    expected_lines = [
        '  - follow: false',
        '    host: hexlet.io',
        '  - proxy: 123.234.53.22',
        '  - timeout: 50',
        '  + timeout: 20',
        '  + verbose: true'
    ]

    for line in expected_lines:
        assert line in result
