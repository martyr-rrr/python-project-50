# Gendiff

[![Tests](https://github.com/martyr-rrr/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/martyr-rrr/python-project-50/actions/workflows/hexlet-check.yml)

A utility for finding differences between configuration files.

## Installation

```bash
uv tool install git+https://github.com/martyr-rrr/python-project-50.git
## Supported formats
- JSON (.json)
- YAML (.yml, .yaml)
## Compare nested structures

```bash
gendiff tests/fixtures/nested/file1.json tests/fixtures/nested/file2.json

## Output formats

### Stylish (default)

```bash
gendiff file1.json file2.json
# or
gendiff --format stylish file1.json file2.json
