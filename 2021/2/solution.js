import fs from 'fs';
import { fileURLToPath } from 'url';
import { dirname } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const input = fs.readFileSync(`${__dirname}/input.txt`, 'utf-8').split('\n');
const data = input.map(v => v.split(' ')).map(v => [v[0], parseInt(v[1])]);

function solution1() {
    let i = 0, j = 0;

    for (const [direction, value] of data) {
        switch (direction) {
            case 'forward':
                j += value;
                break;
            case 'up':
                i -= value;
                break;
            case 'down':
                i += value;
                break;
        }
    }

    return Math.abs(i * j);
}

function solution2() {
    let i = 0, j = 0, aim = 0;

    for (const [direction, value] of data) {
        switch (direction) {
            case 'forward':
                i += value;
                j += aim * value;
                break;
            case 'up':
                aim -= value;
                break;
            case 'down':
                aim += value;
                break;
        }
    }

    return Math.abs(i * j);
}

console.log(solution1());
console.log(solution2());
