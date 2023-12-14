import fs from 'fs';
import { fileURLToPath } from 'url';
import { dirname } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const input = fs.readFileSync(`${__dirname}/input.txt`, 'utf-8')
    .split('\n')
    .map(game => game.split(' '))
    .map(([hand, score]) => [hand, +score]);

const weights = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
};

function getAllJokerCombinations(hand) {
    let result = [ [] ];

    for (let i = 0; i < hand.length; i++) {
        if (hand[i] === 'J') {
            const newResult = [];

            for (const v of result) {
                newResult.push([...v, 'A']);
                newResult.push([...v, 'K']);
                newResult.push([...v, 'Q']);
                newResult.push([...v, 'J']);
                newResult.push([...v, 'T']);
                newResult.push([...v, '9']);
                newResult.push([...v, '8']);
                newResult.push([...v, '7']);
                newResult.push([...v, '6']);
                newResult.push([...v, '5']);
                newResult.push([...v, '4']);
                newResult.push([...v, '3']);
                newResult.push([...v, '2']);
            }

            result = newResult;
        } else {
            for (const v of result) v.push(hand[i]);
        }
    }

    return result.map(v => v.join(''));
}

function getType(hand) {
    const set = new Set(hand.split(''));

    if (set.size === 1) return 10; // five of a kind
    if (set.size === 4) return 5;  // one pair
    if (set.size === 5) return 4;  // high card

    const values = [...set]
        .map(value => hand.split('').filter(v => v === value).length)
        .sort((a, b) => b - a);

    if (set.size === 2 && values[0] === 4) return 9; // four of a kind
    if (set.size === 2 && values[0] === 3) return 8; // full house
    if (set.size === 3 && values[0] === 3) return 7; // three of a kind
    if (set.size === 3 && values[0] === 2) return 6; // two pairs
}

function compare(hand1, hand2) {
    const type1 = getType(hand1);
    const type2 = getType(hand2);

    if (type1 > type2) return 1;
    if (type1 < type2) return -1;

    for (let i = 0; i < hand1.length; i++) {
        const value1 = weights[hand1[i]] ?? +hand1[i];
        const value2 = weights[hand2[i]] ?? +hand2[i];

        if (value1 > value2) return 1;
        if (value1 < value2) return -1;
    }

    return 0;
}

function compareWithJokers(hand1, hand2) {
    const combinations1 = getAllJokerCombinations(hand1);
    const combinations2 = getAllJokerCombinations(hand2);

    const type1 = combinations1.sort((a, b) => getType(b) - getType(a)).at(0);
    const type2 = combinations2.sort((a, b) => getType(b) - getType(a)).at(0);

    return compare(type1, type2);
}

function solution(comparer) {
    return input
        .toSorted(([hand1], [hand2]) => comparer(hand1, hand2))
        .reduce((acc, v, i) => acc + v[1] * (i + 1), 0);
}

const result1 = solution(compare);
console.log(result1); // 253933213

const result2 = solution(compareWithJokers);
console.log(result2); // 253473930
