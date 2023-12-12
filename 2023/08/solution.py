from functools import reduce
import os
dir_path = os.path.dirname(os.path.realpath(__file__))


def lcm(x, y):
    from math import gcd
    return x * y // gcd(x, y)


def solution1(instructions, tree):
    result = 0
    current_node = 'AAA'

    while current_node != 'ZZZ':
        instruction = instructions[result % len(instructions)]

        if instruction == 'L':
            current_node = tree[current_node][0]
        elif instruction == 'R':
            current_node = tree[current_node][1]

        result += 1

    return result


def solution2(instructions, tree):
    result = 0
    nodes = [key for key in tree.keys() if key[2] == 'A']
    cache = [None] * len(nodes)

    # input data has all __A placed on the cycle path
    # and all occurances of __Z nodes happen at a constant rate
    # therefore we can check the first occurance of each __Z node only
    while any(node == None for node in cache):
        instruction = instructions[result % len(instructions)]

        for index, node in enumerate(nodes):
            if node[2] == 'Z':
                cache[index] = result

            if instruction == 'L':
                nodes[index] = tree[node][0]
            elif instruction == 'R':
                nodes[index] = tree[node][1]

        result += 1

    return reduce(lambda x, y: lcm(x, y), cache)


with open(f'{dir_path}/input.txt', 'r') as f:
    data = f.read().split('\n')

    instructions = data[0]
    tree = dict([(row[0:3], (row[7:10], row[12:15])) for row in data[2:]])

    result1 = solution1(instructions, tree)
    print(result1)

    result2 = solution2(instructions, tree)
    print(result2)
