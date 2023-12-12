import os
dir_path = os.path.dirname(os.path.realpath(__file__))


def solution1(data):
    result = 0
    for line in data:
        for char in line:
            if char.isdigit():
                result += int(char) * 10
                break
        for char in reversed(line):
            if char.isdigit():
                result += int(char)
                break
    return result


def solution2(data):
    dict = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

    result = 0
    for line in data:
        for (i, char) in enumerate(line):
            if char.isdigit():
                result += int(char) * 10
                break
            if (dict.get(line[i:i+3])):
                result += dict.get(line[i:i+3]) * 10
                break
            if (dict.get(line[i:i+4])):
                result += dict.get(line[i:i+4]) * 10
                break
            if (dict.get(line[i:i+5])):
                result += dict.get(line[i:i+5]) * 10
                break

        for i in range(len(line) - 1, -1, -1):
            if line[i].isdigit():
                result += int(line[i])
                break
            if (dict.get(line[i-2:i+1])):
                result += dict.get(line[i-2:i+1])
                break
            if (dict.get(line[i-3:i+1])):
                result += dict.get(line[i-3:i+1])
                break
            if (dict.get(line[i-4:i+1])):
                result += dict.get(line[i-4:i+1])
                break
    return result


with open(f'{dir_path}/input.txt', 'r') as f:
    data = f.read().splitlines()

    result1 = solution1(data)
    print(result1)

    result2 = solution2(data)
    print(result2)
