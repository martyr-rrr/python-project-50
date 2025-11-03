def build_diff(data1, data2):
    """
    Строит промежуточное представление diff между двумя структурами
    """
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff = []

    for key in keys:
        node = {'key': key}

        if key not in data2:
            # Ключ удален
            node.update({
                'type': 'removed',
                'value': data1[key]
            })
        elif key not in data1:
            # Ключ добавлен
            node.update({
                'type': 'added',
                'value': data2[key]
            })
        elif data1[key] == data2[key]:
            # Ключ без изменений
            node.update({
                'type': 'unchanged',
                'value': data1[key]
            })
        else:
            # Ключ изменен
            if (isinstance(data1[key], dict) and
                    isinstance(data2[key], dict)):
                # Оба значения - словари, рекурсивно строим diff
                node.update({
                    'type': 'nested',
                    'children': build_diff(data1[key], data2[key])
                })
            else:
                # Значения разные и не оба словари
                node.update({
                    'type': 'changed',
                    'old_value': data1[key],
                    'new_value': data2[key]
                })

        diff.append(node)

    return diff
