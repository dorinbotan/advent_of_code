import os
dir_path = os.path.dirname(os.path.realpath(__file__))


def solution1(data):
    result = 0

    for line in data:
        game = line.split(': ')[1]
        [winning_numbers, my_numbers] = game.split('| ')
        winning_set = set(winning_numbers.split(' '))

        score = 0

        for number in my_numbers.split(' '):
            if number == '':
                continue
            if number in winning_set:
                if score == 0:
                    score = 1
                else:
                    score *= 2

        result += score

    return result


def solution2(data):
    memo = [None] * len(data)

    def traverse(game_id):
        if game_id >= len(data):
            return 0

        if memo[game_id] is None:
            winning_numbers, my_numbers = data[game_id].split(': ')[1].split('| ')
            winning_set = set(winning_numbers.split(' '))
            score = sum(1 for number in my_numbers.split(' ')
                        if number != '' and number in winning_set)

            memo[game_id] = score
            for i in range(game_id + 1, game_id + score + 1):
                memo[game_id] += traverse(i)

        return memo[game_id]

    return sum(1 + traverse(i) for i in range(len(data)))


with open(f'{dir_path}/input.txt', 'r') as f:
    data = f.read().splitlines()

    result1 = solution1(data)
    print(result1)

    result2 = solution2(data)
    print(result2)
