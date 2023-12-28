import os

dir_path = os.path.dirname(os.path.realpath(__file__))


def parse_handler(rule):
    if ':' not in rule:
        return {
            'handler': lambda _: True,
            'direction': rule
        }

    rule, direction = rule.split(':')
    key, value = rule.replace('<', '>').split('>')
    value = int(value)
    op = lambda x, y: x < y if '<' in rule else x > y

    return {
        'handler': lambda part: op(part[key], value),
        'direction': direction,
    }


def parse_rules(rules):
    result = {}

    for rule in rules.splitlines():
        name, rule = rule.split('{')
        rules = rule.strip('}').split(',')
        handlers = [parse_handler(rule) for rule in rules]
        result[name] = handlers

    return result


def parse_parts(parts):
    result = []

    for part in parts.splitlines():
        part = part.strip('{}')
        pairs = part.split(',')
        obj = {}
        for pair in pairs:
            key, value = pair.split('=')
            obj[key] = int(value)
        result.append(obj)

    return result


def get_rating(part):
    return sum(part.values())

with open(f'{dir_path}/input.txt', 'r') as f:
    [rules, parts] = f.read().split('\n\n')
    parts = parse_parts(parts)
    rules = parse_rules(rules)

    result = 0

    for part in parts:
        rule = 'in'

        while rule != 'A' and rule != 'R':
            for check in rules[rule]:
                if check['handler'](part):
                    rule = check['direction']
                    break

        if rule == 'A':
            result += get_rating(part)

    print(result)  # 389114
