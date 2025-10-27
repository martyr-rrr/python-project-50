from gendiff.parsers import read_file


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

    return build_diff(data1, data2)


def build_diff(data1, data2):
    """Генерирует разницу между двумя словарями"""
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff_lines = []

    for key in keys:
        if key not in data2:
            diff_lines.append(f"  - {key}: {format_value(data1[key])}")
        elif key not in data1:
            diff_lines.append(f"  + {key}: {format_value(data2[key])}")
        elif data1[key] == data2[key]:
            diff_lines.append(f"    {key}: {format_value(data1[key])}")
        else:
            diff_lines.append(f"  - {key}: {format_value(data1[key])}")
            diff_lines.append(f"  + {key}: {format_value(data2[key])}")

    if not diff_lines:
        return "{}"

    return "{\n" + "\n".join(diff_lines) + "\n}"


def format_value(value):
    """Форматирует значение для вывода"""
    if isinstance(value, bool):
        return str(value).lower()
    return str(value)
