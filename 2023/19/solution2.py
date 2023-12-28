import os

dir_path = os.path.dirname(os.path.realpath(__file__))


def parse_handler(rule):
    if ':' not in rule:
        return {
            'key': None,
            'value': None,
            'op': None,
            'direction': rule
        }

    rule, direction = rule.split(':')
    key, value = rule.replace('<', '>').split('>')
    value = int(value)
    op = '<' if '<' in rule else '>'

    return {
        'key': key,
        'value': value,
        'op': op,
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


def dp(rules, node='in', x=[0,4001], m=[0,4001], a=[0,4001], s=[0,4001]):
    if node == 'R':
        return 0

    if node == 'A':
        d1 = max(0, x[1] - x[0])
        d2 = max(0, m[1] - m[0])
        d3 = max(0, a[1] - a[0])
        d4 = max(0, s[1] - s[0])
        return d1 * d2 * d3 * d4

    result = 0

    for handler in rules[node]:
        if handler['key'] is None:
            result += dp(rules, handler['direction'], x, m, a, s)
        else:
            # Update weights depending on handler['op'] and call dp
            if handler['op'] == '<':
                if handler['key'] == 'x':
                    result += dp(rules, handler['direction'], [x[0], min(x[1], handler['value'])], m, a, s)
                    x = [max(x[0], handler['value']), x[1]]
                elif handler['key'] == 'm':
                    result += dp(rules, handler['direction'], x, [m[0], min(m[1], handler['value'])], a, s)
                    m = [max(m[0], handler['value']), m[1]]
                elif handler['key'] == 'a':
                    result += dp(rules, handler['direction'], x, m, [a[0], min(a[1], handler['value'])], s)
                    a = [max(a[0], handler['value']), a[1]]
                elif handler['key'] == 's':
                    result += dp(rules, handler['direction'], x, m, a, [s[0], min(s[1], handler['value'])])
                    s = [max(s[0], handler['value']), s[1]]
            else:
                if handler['key'] == 'x':
                    result += dp(rules, handler['direction'], [max(x[0], handler['value'] + 1), x[1]], m, a, s)
                    x = [x[0], min(x[1], handler['value'] + 1)]
                elif handler['key'] == 'm':
                    result += dp(rules, handler['direction'], x, [max(m[0], handler['value'] + 1), m[1]], a, s)
                    m = [m[0], min(m[1], handler['value'] + 1)]
                elif handler['key'] == 'a':
                    result += dp(rules, handler['direction'], x, m, [max(a[0], handler['value'] + 1), a[1]], s)
                    a = [a[0], min(a[1], handler['value'] + 1)]
                elif handler['key'] == 's':
                    result += dp(rules, handler['direction'], x, m, a, [max(s[0], handler['value'] + 1), s[1]])
                    s = [s[0], min(s[1], handler['value'] + 1)]

    return result


with open(f'{dir_path}/test.txt', 'r') as f:
    rules = f.read().split('\n\n')[0]
    rules = parse_rules(rules)

    result = dp(rules)
    print(result)
