from gendiff.core import generate_diff


def test_exact_stylish_format():
    """Тест точного соответствия формату вывода"""
    file1 = 'tests/fixtures/nested/file1.json'
    file2 = 'tests/fixtures/nested/file2.json'

    result = generate_diff(file1, file2)

    # Проверим ключевые элементы формата
    assert '  + follow: false' in result
    assert '    setting1: Value 1' in result
    assert '  - setting2: 200' in result
    assert '  - setting3: true' in result
    assert '  + setting3: null' in result
    assert '  + setting4: blah blah' in result

    # Проверим вложенные структуры
    assert '      key5: value5' in result
    assert '        doge: {' in result
    assert '      - wow:' in result or '      - wow: ' in result
    assert '      + wow: so much' in result
    assert '      + ops: vops' in result

    print("Stylish format test passed!")
    print("\nCurrent output:")
    print(result)
