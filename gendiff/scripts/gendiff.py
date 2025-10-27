#!/usr/bin/env python3
import argparse
import json
from gendiff import generate_diff


def read_file(file_path):
    """Читает и парсит JSON файл"""
    with open(file_path, 'r') as file:
        return json.load(file)


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
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format - {e}")


if __name__ == '__main__':
    main()
