import os

dir_path = os.path.dirname(os.path.realpath(__file__))


# Shoelace formula
def solution(data):
    p1 = (0, 0)

    result = 0

    for row in data:
        p2 = (p1[0], p1[1])

        if row[0] == 'R':
            p2 = (p2[0], p2[1] + row[1])
        elif row[0] == 'L':
            p2 = (p2[0], p2[1] - row[1])
        elif row[0] == 'U':
            p2 = (p2[0] - row[1], p2[1])
        elif row[0] == 'D':
            p2 = (p2[0] + row[1], p2[1])

        # Green's theorem works on points in the counter-clockwise direction
        # so we'll get a negative area here
        result += p1[0] * p2[1] - p1[1] * p2[0]
        # Border should also be counted
        result -= row[1]
        p1 = p2

    return int(abs(result / 2 - 1))


with open(f'{dir_path}/input.txt', 'r') as f:
    DIRECTIONS = {
        '0': 'R',
        '1': 'D',
        '2': 'L',
        '3': 'U',
    }

    data = [
        (
            row.split(' ')[0],
            int(row.split(' ')[1]),
            DIRECTIONS[row.split(' ')[2][-2:-1]],
            int(row.split(' ')[2][2:-2], 16),
        )
        for row in f.read().splitlines()
    ]

    result1 = solution([row[0:2] for row in data])
    print(result1)  # 68115

    result2 = solution([row[2:] for row in data])
    print(result2)  # 71262565063800
