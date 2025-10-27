#!/usr/bin/env python3
import argparse
from gendiff import generate_diff
from gendiff.parsers import get_format, parse_data


def read_file(file_path):
    """Читает и парсит файл"""
    with open(file_path, 'r') as file:
        content = file.read()
        file_format = get_format(file_path)
        return parse_data(content, file_format)


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
        data1 = read_file(args.first_file)
        data2 = read_file(args.second_file)

        diff = generate_diff(data1, data2)
        print(diff)

    except FileNotFoundError as e:
        print(f"Error: File not found - {e}")
    except (ValueError, Exception) as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    main()
