import json
import yaml


def parse_data(data, format_name):
    """Парсит данные в зависимости от формата"""
    if format_name == 'json':
        return json.loads(data)
    elif format_name in ('yaml', 'yml'):
        return yaml.safe_load(data)
    else:
        raise ValueError(f"Unsupported format: {format_name}")


def get_format(file_path):
    """Определяет формат файла по расширению"""
    if file_path.endswith(('.yaml', '.yml')):
        return 'yaml'
    elif file_path.endswith('.json'):
        return 'json'
    else:
        raise ValueError(f"Unsupported file format: {file_path}")


def read_file(file_path):
    """Читает и парсит файл"""
    with open(file_path, 'r') as file:
        content = file.read()
        file_format = get_format(file_path)
        return parse_data(content, file_format)
