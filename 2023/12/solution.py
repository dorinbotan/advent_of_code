import os
dir_path = os.path.dirname(os.path.realpath(__file__))


# Should get counts[0] of '#' or '?' followed by a '.'
def check(map, counts):
    if len(counts) == 0:
        return False

    if len(map) < counts[0]:
        return False

    if len(map) > counts[0] and map[counts[0]] == '#':
        return False

    for i in range(counts[0]):
        if map[i] == '.':
            return False

    return True


def dp(map, counts, cache=None):
    if cache is None:
        cache = dict()

    key = (len(map), len(counts))

    if key in cache:
        return cache[key]

    if len(map) == 0:
        cache[key] = 1 if len(counts) == 0 else 0
    elif map[0] == '.':
        cache[key] = dp(map[1:], counts, cache)
    elif map[0] == '#':
        cache[key] = dp(map[counts[0] + 1:], counts[1:], cache) if check(map, counts) else 0
    elif map[0] == '?':
        cache[key] = dp(map[1:], counts, cache) + (
            dp(map[counts[0] + 1:], counts[1:], cache) if check(map, counts) else 0
        )

    return cache[key]


def solution(data, n=1):
    result = 0

    for map, counts in data:
        result += dp('?'.join([map] * n), counts * n)

    return result


with open(f'{dir_path}/input.txt', 'r') as f:
    data = [
        [row.split(' ')[0], [int(col) for col in row.split(' ')[1].split(',')]]
        for row in f.read().split('\n')
    ]

    result1 = solution(data, 1)  # 7221
    print(result1)

    result2 = solution(data, 5)  # 7139671893722
    print(result2)
