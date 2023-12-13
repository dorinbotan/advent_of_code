import os
dir_path = os.path.dirname(os.path.realpath(__file__))


def get_horizontal_reflection(tile, errors):
    def check(x, errors=0):
        reflection_height = min(x, len(tile) - x)

        for i in range(x - reflection_height, x):
            for j in range(len(tile[0])):
                up = tile[i][j]
                down = tile[x + x - i - 1][j]

                if up != down:
                    if errors <= 0:
                        return False
                    errors -= 1

        return errors == 0

    for x in range(1, len(tile)):
        if check(x, errors):
            return x

    return None


def get_vertical_reflection(tile, errors):
    def check(x, errors=0):
        reflection_width = min(x, len(tile[0]) - x)

        for i in range(len(tile)):
            for j in range(x - reflection_width, x):
                left = tile[i][j]
                right = tile[i][x + x - j - 1]

                if left != right:
                    if errors <= 0:
                        return False
                    errors -= 1

        return errors == 0

    for x in range(1, len(tile[0])):
        if check(x, errors):
            return x

    return None


def solution(data, errors):
    result = 0

    for tile in data:
        vertical = get_vertical_reflection(tile, errors)
        horizontal = get_horizontal_reflection(tile, errors)

        if vertical is not None:
            result += vertical

        if horizontal is not None:
            result += horizontal * 100

    return result


with open(f'{dir_path}/input.txt', 'r') as f:
    data = [
        tile.split('\n')
        for tile in f.read().split('\n\n')
    ]

    result1 = solution(data, 0)  # 37561
    print(result1)

    result2 = solution(data, 1)  # 31108
    print(result2)
