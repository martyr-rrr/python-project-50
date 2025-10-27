import json


def render(diff):
    """Основная функция рендеринга JSON формата"""
    return json.dumps(diff, indent=2)
