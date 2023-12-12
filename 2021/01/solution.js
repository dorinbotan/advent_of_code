import fs from 'fs';
import { fileURLToPath } from 'url';
import { dirname } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const input = fs.readFileSync(`${__dirname}/input.txt`, 'utf-8').split('\n');

function solution1() {
    let result = 0;

    for (let i = 1; i in input; i++) {
        if (+input[i] > +input[i - 1]) result++;
    }

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
