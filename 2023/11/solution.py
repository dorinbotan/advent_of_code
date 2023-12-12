import os
dir_path = os.path.dirname(os.path.realpath(__file__))


def get_empty_prefix_sums(data):
    empty_row = [True] * (len(data))
    empty_col = [True] * (len(data[0]))

    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == '#':
                empty_row[i] = False
                empty_col[j] = False

    row_prefix_sums = [0] * (len(data))
    col_prefix_sums = [0] * (len(data[0]))

    for i in range(1, len(empty_row)):
        row_prefix_sums[i] = row_prefix_sums[i - 1] + empty_row[i]

    for i in range(1, len(empty_col)):
        col_prefix_sums[i] = col_prefix_sums[i - 1] + empty_col[i]

    return row_prefix_sums, col_prefix_sums


def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def check(galaxy, root, row_prefix_sums, col_prefix_sums, weight):
    result = 0

    for i in range(len(galaxy)):
        for j in range(len(galaxy[0])):
            if galaxy[i][j] == '.':
                continue

            result += manhattan_distance((i, j), root)
            result += (row_prefix_sums[max(i, root[0])] - row_prefix_sums[min(i, root[0])]) * weight
            result += (col_prefix_sums[max(j, root[1])] - col_prefix_sums[min(j, root[1])]) * weight

    return result


def solution(galaxy, row_prefix_sums, col_prefix_sums, weight):
    result = 0

    for i in range(len(galaxy)):
        for j in range(len(galaxy[0])):
            if galaxy[i][j] == '#':
                result += check(galaxy, (i, j), row_prefix_sums, col_prefix_sums, weight)

    return result // 2


with open(f'{dir_path}/input.txt', 'r') as f:
    galaxy = f.read().split('\n')

    row_prefix_sums, col_prefix_sums = get_empty_prefix_sums(galaxy)

    # 9723824
    result1 = solution(galaxy, row_prefix_sums, col_prefix_sums, 1)
    print(result1)

    # 731244261352
    result2 = solution(galaxy, row_prefix_sums, col_prefix_sums, 999999)
    print(result2)
