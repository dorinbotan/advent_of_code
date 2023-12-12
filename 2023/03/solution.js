import fs from 'fs';
import { fileURLToPath } from 'url';
import { dirname } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const input = fs.readFileSync(`${__dirname}/input.txt`, 'utf-8').split('\n');

function isSymbol(char) {
    return char && char !== '.' && Number.isNaN(+char);
}

function getNumber(i, j) {
    const number = [];
    const details = new Map();

    while (Number.isInteger(+input[i][j])) {
        number.push(input[i][j]);

        [
            [i, j + 1],
            [i + 1, j],
            [i, j - 1],
            [i - 1, j],
            [i - 1, j - 1],
            [i - 1, j + 1],
            [i + 1, j - 1],
            [i + 1, j + 1],
        ].forEach(([i, j]) => {
            if (isSymbol(input[i]?.[j])) {
                details.set(`${i}:${j}`, input[i][j]);
            }
        });

        j++;
    }

    let d = [...details];

    if (!d.length) return [];

    return [number, d];
}

function solution1() {
    let result = 0;

    for (let i = 0; i < input.length; i++) {
        const row = input[i];

        for (let j = 0; j < row.length; j++) {
            const char = row[j];

            if (Number.isNaN(+char)) continue;

            const [number] = getNumber(i, j);

            if (number) {
                result += +number.join('');
                j += number.length - 1;
            }
        }
    }

    return result;
}

function solution2() {
    const gears = new Map();

    for (let i = 0; i < input.length; i++) {
        const row = input[i];

        for (let j = 0; j < row.length; j++) {
            const char = row[j];

            if (Number.isNaN(+char)) continue;

            const [number, details] = getNumber(i, j);

            if (number) {
                for (const [key, char] of details) {
                    if (char !== '*') continue;

                    if (!gears.has(key)) {
                        gears.set(key, []);
                    }

                    gears.get(key).push(+number.join(''));
                }

                j += number.length - 1;
            }
        }
    }

    const match = [...gears]
        .filter(([, values]) => values.length === 2)
        .reduce((acc, [key, values]) => {
            return acc + values[0] * values[1];
        }, 0);

    return match;
}

console.log(solution1()); // 537832
console.log(solution2()); // 81939900
