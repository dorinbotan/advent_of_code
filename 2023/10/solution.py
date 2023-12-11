import sys
sys.setrecursionlimit(10000)

import os
dir_path = os.path.dirname(os.path.realpath(__file__))


def find_element(matrix, element):
    for i, row in enumerate(matrix):
        if element in row:
            j = row.index(element)
            return i, j
    return None


def spread(matrix, start):
    result = [['#' for x in range(len(matrix[0]) * 2 - 1)] for _ in range(len(matrix) * 2 - 1)]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[i * 2][j * 2] = matrix[i][j]

            if i < (len(matrix) - 1):
                if (matrix[i][j] == 'F') or (
                    matrix[i][j] == '|') or (
                    matrix[i][j] == '7'):
                    result[i * 2 + 1][j * 2] = '|'
                else:
                    result[i * 2 + 1][j * 2] = ' '

            if j < (len(matrix[0]) - 1):
                if (matrix[i][j] == 'F') or (
                    matrix[i][j] == '-') or (
                    matrix[i][j] == 'L'):
                    result[i * 2][j * 2 + 1] = '-'
                else:
                    result[i * 2][j * 2 + 1] = ' '

            if (i < (len(matrix) - 1)) and (j < (len(matrix[0]) - 1)):
                result[i * 2 + 1][j * 2 + 1] = ' '

    # special case for S
    if start[0] < len(matrix) - 1 and matrix[start[0] + 1][start[1]] in ['L', '|', 'J']:
        result[start[0] * 2 + 1][start[1] * 2] = '|'

    if start[1] < len(matrix[0]) - 1 and matrix[start[0]][start[1] + 1] in ['7', '-', 'J']:
        result[start[0] * 2][start[1] * 2 + 1] = '-'

    return result


def get_moves(map, pos, visited):
    result = []

    #       7 | F
    # F - L       7 - J
    #       L | J

    up = ['7', '|', 'F']
    down = ['L', '|', 'J']
    left = ['F', '-', 'L']
    right = ['7', '-', 'J']

    moves = {
        'S': {
            'up': up,
            'down': down,
            'left': left,
            'right': right,
        },
        '-': {
            'up': [],
            'down': [],
            'left': left,
            'right': right,
        },
        '|': {
            'up': up,
            'down': down,
            'left': [],
            'right': [],
        },
        '7': {
            'up': [],
            'down': down,
            'left': left,
            'right': [],
        },
        'J': {
            'up': up,
            'down': [],
            'left': left,
            'right': [],
        },
        'L': {
            'up': up,
            'down': [],
            'left': [],
            'right': right,
        },
        'F': {
            'up': [],
            'down': down,
            'left': [],
            'right': right,
        },
    }

    if pos[0] > 0 and map[pos[0] - 1][pos[1]] in moves[map[pos[0]][pos[1]]]['up']:
        result.append((pos[0] - 1, pos[1]))

    if pos[0] < len(map) - 1 and map[pos[0] + 1][pos[1]] in moves[map[pos[0]][pos[1]]]['down']:
        result.append((pos[0] + 1, pos[1]))

    if pos[1] > 0 and map[pos[0]][pos[1] - 1] in moves[map[pos[0]][pos[1]]]['left']:
        result.append((pos[0], pos[1] - 1))

    if pos[1] < len(map[0]) - 1 and map[pos[0]][pos[1] + 1] in moves[map[pos[0]][pos[1]]]['right']:
        result.append((pos[0], pos[1] + 1))

    return [value for value in result if value not in visited]


def bfs(map, pos, visited):
    # for (a, b) in visited:
    #     map[a][b] = '#'

    # out = [''.join(row) for row in map]

    if pos[0] < 0 or pos[0] >= len(map) or pos[1] < 0 or pos[1] >= len(map[0]):
        return 0

    visited.add(pos)

    result = 0

    if pos[0] % 2 == 0 and pos[1] % 2 == 0:
        result += 1

    if (pos[0] - 1, pos[1]) not in visited:
        result += bfs(map, (pos[0] - 1, pos[1]), visited)

    if (pos[0] + 1, pos[1]) not in visited:
        result += bfs(map, (pos[0] + 1, pos[1]), visited)

    if (pos[0], pos[1] - 1) not in visited:
        result += bfs(map, (pos[0], pos[1] - 1), visited)

    if (pos[0], pos[1] + 1) not in visited:
        result += bfs(map, (pos[0], pos[1] + 1), visited)

    return result


def solution1(map, start):
    visited = set([start])
    [p1, p2] = get_moves(map, start, visited)
    distance = 1

    while p1 and p2 and p1 != p2:
        visited.add(p1)
        visited.add(p2)

        p1 = get_moves(map, p1, visited)[0]
        p2 = get_moves(map, p2, visited)[0]
        distance += 1

    return distance


def solution2(map, start):
    map = spread(map, start)
    start = (start[0] * 2, start[1] * 2)

    loop = set([start])
    [p1, p2] = get_moves(map, start, loop)

    while p1 and p2 and p1 != p2:
        loop.add(p1)
        loop.add(p2)

        p1 = get_moves(map, p1, loop)[0]
        p2 = get_moves(map, p2, loop)[0]

    loop.add(p1)

    # Use any point inside the loop as the second argument
    # it can be found with the even/odd rule or where's wally approach
    return bfs(map, (start[0] + 1, start[1] + 1), loop)


with open(f'{dir_path}/input.txt', 'r') as f:
    map = f.read().split('\n')
    start = find_element(map, 'S')

    result1 = solution1(map, start) # 7005
    print(result1)

    result2 = solution2(map, start) # 417
    print(result2)
