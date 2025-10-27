def stringify(value):
    """Преобразует значение в строку для plain формата"""
    if isinstance(value, (dict, list)):
        return '[complex value]'
    elif isinstance(value, str):
        return f"'{value}'"
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    else:
        return str(value)


def build_path(current_path, key):
    """Строит полный путь до свойства"""
    if current_path:
        return f"{current_path}.{key}"
    return key


def format_diff(diff, path=''):
    """Форматирует diff в plain формате"""
    lines = []
    for node in diff:
        key = node['key']
        node_type = node['type']
        current_path = build_path(path, key)
        if node_type == 'nested':
            children_lines = format_diff(node['children'], current_path)
            lines.extend(children_lines)
        elif node_type == 'added':
            value = stringify(node['value'])
            lines.append(
                f"Property '{current_path}' was added with value: {value}"
            )
        elif node_type == 'removed':
            lines.append(f"Property '{current_path}' was removed")
        elif node_type == 'changed':
            old_value = stringify(node['old_value'])
            new_value = stringify(node['new_value'])
            lines.append(
                f"Property '{current_path}' was updated. From {old_value} to {new_value}"  # noqa: E501
            )
    return lines


def render(diff):
    """Основная функция рендеринга plain формата"""
    lines = format_diff(diff)
    return '\n'.join(lines)
