import fs from 'fs';
import { fileURLToPath } from 'url';
import { dirname } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const input = fs.readFileSync(`${__dirname}/input.txt`, 'utf-8').split('\n');

function solution1() {
    let result = 0;

    for (const row of input) {
        for (let i = 0; i < row.length; i++) {
            if (!Number.isInteger(parseInt(row[i]))) continue;
            result += parseInt(row[i]) * 10;
            break;
        }

        for (let i = row.length - 1; i >= 0; i--) {
            if (!Number.isInteger(parseInt(row[i]))) continue;
            result += parseInt(row[i]);
            break;
        }
    }

    return result;
}

function solution2() {
    let result = 0;

    const numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'];

    for (const row of input) {
        for (let i = 0; i < row.length; i++) {
            if (Number.isInteger(parseInt(row[i]))) {
                result += parseInt(row[i]) * 10;
                break;
            }

            if (numbers.some(number => row.slice(i, i + number.length) === number)) {
                result += (numbers.findIndex(number => row.slice(i, i + number.length) === number) + 1) * 10;
                break;
            }
        }

        for (let i = row.length - 1; i >= 0; i--) {
            if (Number.isInteger(parseInt(row[i]))) {
                result += parseInt(row[i]);
                break;
            }

            if (numbers.some(number => row.slice(i - number.length + 1, i + 1) === number)) {
                result += (numbers.findIndex(number => row.slice(i - number.length + 1, i + 1) === number) + 1);
                break;
            }
        }
    }

    return result;
}

console.log(solution1());
console.log(solution2());
