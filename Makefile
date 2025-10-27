install:
	uv sync

test:
	uv run pytest

lint:
	uv run flake8 gendiff tests

check: lint test

.PHONY: install test lint check
