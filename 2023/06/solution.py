import os
import re
dir_path = os.path.dirname(os.path.realpath(__file__))


def solution1(times, distances):
    result = 1

    for time, distance in zip(times, distances):
        valid_solutions = 0

        for speed in range(0, time):
            traversed = speed * (time - speed)
            if traversed > distance:
                valid_solutions += 1

        result *= valid_solutions

    return result


# Can binary search for the upper and lower bounds of the speed
# for logarithmic time complexity
def solution2(times, distances):
    max_time = int(''.join([str(t) for t in times]))
    max_distance = int(''.join([str(t) for t in distances]))

    result = 0

    for speed in range(0, max_time):
        traversed = speed * (max_time - speed)
        if traversed > max_distance:
            result += 1

    return result


def parse(template, data):
    pattern = re.compile(f'{template}([\\d ]+)')
    match = pattern.search(data).group(1).split(' ')
    return [int(x) for x in match if x]


with open(f'{dir_path}/input.txt', 'r') as f:
    data = f.read()

    times = parse('Time: ', data)
    distances = parse('Distance: ', data)

    result1 = solution1(times, distances)
    print(result1)

    result2 = solution2(times, distances)
    print(result2)
