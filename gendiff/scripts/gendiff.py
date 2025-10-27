#!/usr/bin/env python3
import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    
    args = parser.parse_args()
    # Пока просто выводим имена файлов, функциональность добавим позже
    print(f"Comparing {args.first_file} and {args.second_file}")


if __name__ == '__main__':
    main()
