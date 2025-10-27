def stringify(value, depth):
    """Преобразует значение в строку с правильными отступами"""
    if isinstance(value, dict):
        lines = []
        indent = '    ' * depth
        for key, val in sorted(value.items()):
            formatted_value = stringify(val, depth + 1)
            lines.append(f"{indent}    {key}: {formatted_value}")
        if lines:
            return "{\n" + "\n".join(lines) + "\n" + indent + "}"
        else:
            return "{}"
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return str(value)


def format_diff(diff, depth=0):
    """Форматирует diff в stylish формате"""
    if not diff:
        return "{}"
    lines = []
    indent = '    ' * depth
    for node in diff:
        key = node['key']
        node_type = node['type']
        if node_type == 'nested':
            children = format_diff(node['children'], depth + 1)
            lines.append(f"{indent}    {key}: {children}")
        elif node_type == 'added':
            value = stringify(node['value'], depth + 1)
            lines.append(f"{indent}  + {key}: {value}")
        elif node_type == 'removed':
            value = stringify(node['value'], depth + 1)
            lines.append(f"{indent}  - {key}: {value}")
        elif node_type == 'changed':
            old_value = stringify(node['old_value'], depth + 1)
            new_value = stringify(node['new_value'], depth + 1)
            lines.append(f"{indent}  - {key}: {old_value}")
            lines.append(f"{indent}  + {key}: {new_value}")
        elif node_type == 'unchanged':
            value = stringify(node['value'], depth + 1)
            lines.append(f"{indent}    {key}: {value}")
    if depth == 0:
        return "{\n" + "\n".join(lines) + "\n}"
    else:
        return "{\n" + "\n".join(lines) + "\n" + indent + "}"


def render(diff):
    """Основная функция рендеринга stylish формата"""
    return format_diff(diff)
