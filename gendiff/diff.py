def generate_diff(data1, data2):
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
    
    return "{\n" + "\n".join(diff_lines) + "\n}"


def format_value(value):
    """Форматирует значение для вывода"""
    if isinstance(value, bool):
        return str(value).lower()
    return str(value)
