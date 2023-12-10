import os
dir_path = os.path.dirname(os.path.realpath(__file__))


def get_next(row):
    queue = [row]

    while any([value for value in queue[-1] if value != 0]):
        next = []

        for i in range(1, len(queue[-1])):
            next.append(queue[-1][i] - queue[-1][i - 1])

        queue.append(next)

    for i in range(len(queue) - 2, -1, -1):
        queue[i].append(queue[i][-1] + queue[i + 1][-1])

    return queue[0][-1]


def solution1(data):
    result = 0

    for row in data:
        result += get_next(row)

    return result


def solution2(data):
    data = [list(reversed(row)) for row in data]

    result = 0

    for row in data:
        result += get_next(row)

    return result


with open(f'{dir_path}/input.txt', 'r') as f:
    data = [[int(cell) for cell in row.split(' ')] for row in f.read().split('\n')]

    result1 = solution1(data) # 2043183816
    print(result1)

    result2 = solution2(data) # 1118
    print(result2)
