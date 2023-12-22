import os
import sys

sys.setrecursionlimit(500000)
dir_path = os.path.dirname(os.path.realpath(__file__))

INFINITY = 2**64
DIRECTIONS = {
    'U': 0,
    'R': 1,
    'D': 2,
    'L': 3,
}


def get_key(queue):
    if len(queue) > 2 and queue[-1] == queue[-2] == queue[-3]:
        return 8 + queue[-1]  # UUU, RRR, DDD, LLL

    if len(queue) > 1 and queue[-1] == queue[-2]:
        return 4 + queue[-1]  # _UU, _RR, _DD, _LL

    return queue[-1]  # __U, __R, __D, __L


def dp(data, i, j, cache, queue, distance):
    key = get_key(queue)
    map = cache[key]

    if map[i][j] <= distance:
        return

    map[i][j] = distance

    if queue[-1] == DIRECTIONS['R']:
        # dp up
        if i > 0:
            dp(data, i - 1, j, cache, [DIRECTIONS['U']], distance + data[i - 1][j])
        # dp down
        if i < len(data) - 1:
            dp(data, i + 1, j, cache, [DIRECTIONS['D']], distance + data[i + 1][j])
        # dp right
        if key < 8 and j < len(data[0]) - 1:
            dp(data, i, j + 1, cache, queue + [DIRECTIONS['R']], distance + data[i][j + 1])
    elif queue[-1] == DIRECTIONS['D']:
        # dp left
        if j > 0:
            dp(data, i, j - 1, cache, [DIRECTIONS['L']], distance + data[i][j - 1])
        # dp right
        if j < len(data[0]) - 1:
            dp(data, i, j + 1, cache, [DIRECTIONS['R']], distance + data[i][j + 1])
        # dp down
        if key < 8 and i < len(data) - 1:
            dp(data, i + 1, j, cache, queue + [DIRECTIONS['D']], distance + data[i + 1][j])
    elif queue[-1] == DIRECTIONS['L']:
        # dp up
        if i > 0:
            dp(data, i - 1, j, cache, [DIRECTIONS['U']], distance + data[i - 1][j])
        # dp down
        if i < len(data) - 1:
            dp(data, i + 1, j, cache, [DIRECTIONS['D']], distance + data[i + 1][j])
        # dp left
        if key < 8 and j > 0:
            dp(data, i, j - 1, cache, queue + [DIRECTIONS['L']], distance + data[i][j - 1])
    elif queue[-1] == DIRECTIONS['U']:
        # dp left
        if j > 0:
            dp(data, i, j - 1, cache, [DIRECTIONS['L']], distance + data[i][j - 1])
        # dp right
        if j < len(data[0]) - 1:
            dp(data, i, j + 1, cache, [DIRECTIONS['R']], distance + data[i][j + 1])
        # dp up
        if key < 8 and i > 0:
            dp(data, i - 1, j, cache, queue + [DIRECTIONS['U']], distance + data[i - 1][j])


def solution1(data):
    cache = {}

    for i in range(3):
        for j in DIRECTIONS.values():
            key = get_key([j] * (i + 1))
            cache[key] = [[INFINITY] * len(row) for row in data]
            cache[key][0][0] = 0

    dp(data, 0, 1, cache, [DIRECTIONS['R']], data[0][1])
    dp(data, 1, 0, cache, [DIRECTIONS['D']], data[1][0])

    result = INFINITY

    for i in range(3):
        for j in DIRECTIONS.values():
            key = get_key([j] * (i + 1))
            result = min(result, cache[key][-1][-1])

    return result


def solution2(data):
    pass


with open(f'{dir_path}/input.txt', 'r') as f:
    data = [
        [int(value) for value in row]
        for row in f.read().splitlines()
    ]

    result1 = solution1(data)
    print(result1)

    result2 = solution2(data)
    print(result2)
