from gendiff.parsers import read_file
from gendiff.diff_builder import build_diff
from gendiff.formatters import stylish


def generate_diff(file_path1, file_path2, format_name='stylish'):
    """Генерирует разницу между двумя файлами или словарями"""
    # Если переданы пути к файлам - читаем их
    if isinstance(file_path1, str) and isinstance(file_path2, str):
        data1 = read_file(file_path1)
        data2 = read_file(file_path2)
    else:
        # Если переданы уже готовые данные
        data1 = file_path1
        data2 = file_path2

    diff = build_diff(data1, data2)

    # Выбираем форматер
    if format_name == 'stylish':
        return stylish(diff)
    else:
        raise ValueError(f"Unsupported format: {format_name}")


def format_value(value):
    """Форматирует значение для вывода (для обратной совместимости)"""
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    return str(value)
