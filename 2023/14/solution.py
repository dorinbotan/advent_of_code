import os
import hashlib
dir_path = os.path.dirname(os.path.realpath(__file__))


def get_hash(data):
    key = ''.join(data).encode()
    return hashlib.md5(key).hexdigest()


def roll_line(line):
    stack = []

    for value in line:
        if value == '#':
            stack.append(['#', 1])
            pass
        elif value == 'O':
            if len(stack) == 0 or stack[-1][0] == '#':
                stack.append(['O', 1])
            elif stack[-1][0] == 'O':
                stack[-1][1] += 1
            elif len(stack) > 1 and stack[-2][0] == 'O':
                stack[-2][1] += 1
            else:
                last = stack.pop()
                if len(stack) > 0 and stack[-1][0] == 'O':
                    stack[-1][1] += 1
                else:
                    stack.append(['O', 1])
                stack.append(last)
        elif value == '.':
            if len(stack) > 0 and stack[-1][0] == '.':
                stack[-1][1] += 1
            else:
                stack.append(['.', 1])

    return ''.join([segment * length for segment, length in stack])


def roll_N(data):
    columns = [[] for _ in range(len(data[0]))]

    for i in range(len(data)):
        for j in range(len(data[i])):
            columns[j].append(data[i][j])

    for j in range(len(columns)):
        columns[j] = roll_line(columns[j])

    # flip columns around the diagonal
    return [
        ''.join([row[i] for row in columns])
        for i in range(len(columns[0]))
    ]


def roll_S(data):
    columns = [[] for _ in range(len(data[0]))]

    for i in range(len(data) - 1, -1, -1):
        for j in range(len(data[i])):
            columns[j].append(data[i][j])

    for j in range(len(columns)):
        columns[j] = roll_line(columns[j])[::-1]

    # flip columns around the diagonal
    return [
        ''.join([row[i] for row in columns])
        for i in range(len(columns[0]))
    ]


def roll_W(data):
    return [roll_line(row) for row in data]


def roll_E(data):
    return [roll_line(row[::-1])[::-1] for row in data]


def solution(data, steps=1):
    rolled = [row for row in data]
    cache = dict()

    step = 0
    while step < steps:
        hash = get_hash(rolled)
        if hash in cache:
            distance = step - cache[hash]
            can_fit = (steps - cache[hash]) // distance
            step = cache[hash] + distance * can_fit
            del cache[hash]
        else:
            cache[hash] = step
            rolled = roll_N(rolled)
            rolled = roll_W(rolled)
            rolled = roll_S(rolled)
            rolled = roll_E(rolled)
            step += 1

    result = 0
    for i in range(len(rolled)):
        for j in range(len(rolled[i])):
            if rolled[i][j] == 'O':
                result += len(rolled) - i
    return result


with open(f'{dir_path}/input.txt', 'r') as f:
    data = f.read().split('\n')

    result1 = solution(data)  # 103614
    print(result1)

    result2 = solution(data, 1000000000)  # 83790
    print(result2)
