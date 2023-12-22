import sys
import os

sys.setrecursionlimit(10000)
dir_path = os.path.dirname(os.path.realpath(__file__))


DIRECTIONS = {
    'RIGHT': 0b0001,
    'DOWN':  0b0010,
    'LEFT':  0b0100,
    'UP':    0b1000,
}


def dp(data, i, j, direction, visited):
    if i < 0 or i >= len(data) or j < 0 or j >= len(data[0]):
        return

    if bool(visited[i][j] & direction):
        return

    visited[i][j] |= direction

    if data[i][j] == '.':
        if direction == DIRECTIONS['RIGHT']:
            dp(data, i, j+1, direction, visited)
        elif direction == DIRECTIONS['DOWN']:
            dp(data, i+1, j, direction, visited)
        elif direction == DIRECTIONS['LEFT']:
            dp(data, i, j-1, direction, visited)
        elif direction == DIRECTIONS['UP']:
            dp(data, i-1, j, direction, visited)
    elif data[i][j] == '\\':
        if direction == DIRECTIONS['RIGHT']:
            dp(data, i+1, j, DIRECTIONS['DOWN'], visited)
        elif direction == DIRECTIONS['DOWN']:
            dp(data, i, j+1, DIRECTIONS['RIGHT'], visited)
        elif direction == DIRECTIONS['LEFT']:
            dp(data, i-1, j, DIRECTIONS['UP'], visited)
        elif direction == DIRECTIONS['UP']:
            dp(data, i, j-1, DIRECTIONS['LEFT'], visited)
    elif data[i][j] == '/':
        if direction == DIRECTIONS['RIGHT']:
            dp(data, i-1, j, DIRECTIONS['UP'], visited)
        elif direction == DIRECTIONS['DOWN']:
            dp(data, i, j-1, DIRECTIONS['LEFT'], visited)
        elif direction == DIRECTIONS['LEFT']:
            dp(data, i+1, j, DIRECTIONS['DOWN'], visited)
        elif direction == DIRECTIONS['UP']:
            dp(data, i, j+1, DIRECTIONS['RIGHT'], visited)
    elif data[i][j] == '-':
        if direction == DIRECTIONS['RIGHT']:
            dp(data, i, j+1, direction, visited)
        elif direction == DIRECTIONS['DOWN']:
            dp(data, i, j+1, DIRECTIONS['RIGHT'], visited)
            dp(data, i, j-1, DIRECTIONS['LEFT'], visited)
        elif direction == DIRECTIONS['LEFT']:
            dp(data, i, j-1, direction, visited)
        elif direction == DIRECTIONS['UP']:
            dp(data, i, j+1, DIRECTIONS['RIGHT'], visited)
            dp(data, i, j-1, DIRECTIONS['LEFT'], visited)
    elif data[i][j] == '|':
        if direction == DIRECTIONS['RIGHT']:
            dp(data, i+1, j, DIRECTIONS['DOWN'], visited)
            dp(data, i-1, j, DIRECTIONS['UP'], visited)
        elif direction == DIRECTIONS['DOWN']:
            dp(data, i+1, j, direction, visited)
        elif direction == DIRECTIONS['LEFT']:
            dp(data, i+1, j, DIRECTIONS['DOWN'], visited)
            dp(data, i-1, j, DIRECTIONS['UP'], visited)
        elif direction == DIRECTIONS['UP']:
            dp(data, i-1, j, direction, visited)


def count_activated(data, i=0, j=0, direction=DIRECTIONS['RIGHT']):
    visited = [[0 for _ in row] for row in data]

    dp(data, i, j, direction, visited)

    return sum([
        sum([1 for v in row if v != 0])
        for row in visited
    ])


def find_max_activated(data):
    result = 0

    for i in range(len(data)):
        result = max(
            result,
            count_activated(data, i, 0, DIRECTIONS['RIGHT']),
            count_activated(data, i, len(data[0]) - 1, DIRECTIONS['LEFT'])
        )

    for j in range(len(data[0])):
        result = max(
            result,
            count_activated(data, 0, j, DIRECTIONS['DOWN']),
            count_activated(data, len(data) - 1, j, DIRECTIONS['UP'])
        )

    return result


with open(f'{dir_path}/input.txt', 'r') as f:
    data = f.read().splitlines()

    result1 = count_activated(data)  # 8323
    print(result1)

    result2 = find_max_activated(data)  # 8491
    print(result2)
