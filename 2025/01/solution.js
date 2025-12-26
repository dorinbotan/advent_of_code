import fs from 'fs';
import { fileURLToPath } from 'url';
import { dirname } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const input = fs.readFileSync(`${__dirname}/input.txt`, 'utf-8').split('\n');

const data = input.map(v => ({
    direction: v[0] === 'R' ? 1 : -1,
    distance: +v.substr(1),
})).map(({direction, distance}) => direction * distance);

function solution1() {
    let result = 0;
    let pointer = 50;

    for (const v of data) {
        pointer += v;
        if (pointer % 100 === 0) {
            result++;
        }
    }

    console.log(data);

    return result;
}

function solution2() {
    let result = 0;

    for (let i = 3; i in input; i++) {
        const v1 = +input[i - 3] + +input[i - 2] + +input[i - 1];
        const v2 = +input[i - 2] + +input[i - 1] + +input[i];
        if (v2 > v1) result++;
    }


    return result;
}

console.log(solution1());
console.log(solution2());
