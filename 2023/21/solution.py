import os

dir_path = os.path.dirname(os.path.realpath(__file__))


def find_start(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 'S':
                return (i, j)


def solution1(data, steps=64):
    cache = [[0] * len(row) for row in data]

    def dfs(i, j, steps):
        if 1 << steps & cache[i][j]:
            return
        cache[i][j] |= 1 << steps

        if not steps:
            return

        if i > 0 and data[i - 1][j] != '#':
            dfs(i - 1, j, steps - 1)

        if i < len(data) - 1 and data[i + 1][j] != '#':
            dfs(i + 1, j, steps - 1)

        if j > 0 and data[i][j - 1] != '#':
            dfs(i, j - 1, steps - 1)

        if j < len(data[i]) - 1 and data[i][j + 1] != '#':
            dfs(i, j + 1, steps - 1)

    dfs(*find_start(data), steps)

    return sum([
        len([value for value in row if value & 1])
        for row in cache
    ])


def solution2(data):
    pass


with open(f'{dir_path}/input.txt', 'r') as f:
    data = f.read().splitlines()

    result1 = solution1(data, 64)  # 3748
    print(result1)

    result2 = solution2(data)
    print(result2)
