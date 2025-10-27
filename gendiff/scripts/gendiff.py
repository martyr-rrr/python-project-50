#!/usr/bin/env python3
import argparse
import json


def read_file(file_path):
    """Читает и парсит JSON файл"""
    with open(file_path, 'r') as file:
        return json.load(file)


def generate_diff(file_path1, file_path2, format_name='stylish'):
    """Генерирует разницу между двумя файлами"""
    data1 = read_file(file_path1)
    data2 = read_file(file_path2)
    
    # Пока просто возвращаем данные, сравнение добавим позже
    return {
        'file1_data': data1,
        'file2_data': data2,
        'format': format_name
    }


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        help='set format of output',
                        default='stylish')
    
    args = parser.parse_args()
    
    try:
        result = generate_diff(args.first_file, args.second_file, args.format)
        print("First file data:", result['file1_data'])
        print("Second file data:", result['file2_data'])
        print(f"Output format: {result['format']}")
        
    except FileNotFoundError as e:
        print(f"Error: File not found - {e}")
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format - {e}")


if __name__ == '__main__':
    main()
