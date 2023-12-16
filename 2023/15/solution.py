import os
import re
dir_path = os.path.dirname(os.path.realpath(__file__))


def get_hash(data):
    result = 0

    for char in data:
        result += ord(char)
        result = result * 17 % 256

    return result


def solution1(data):
    return sum([get_hash(''.join(row)) for row in data])


def solution2(data):
    focal_lengths = dict()
    boxes = [[] for _ in range(256)]

    for label, op, f in data:
        box = get_hash(label)

        if op == '-':
            if label in focal_lengths:
                del focal_lengths[label]

            if label in boxes[box]:
                boxes[box].remove(label)
        elif op == '=':
            focal_lengths[label] = int(f)

            if label not in boxes[box]:
                boxes[box].append(label)

    result = 0

    for i, box in enumerate(boxes):
        for j, label in enumerate(box):
            result += (i + 1) * (j + 1) * focal_lengths[label]

    return result


with open(f'{dir_path}/input.txt', 'r') as f:
    data = re.findall(r'([a-z]+)([-=]{1})([\d]*)', f.read())

    result1 = solution1(data)  # 510013
    print(result1)

    result2 = solution2(data)  # 268497
    print(result2)
