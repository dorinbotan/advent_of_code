import fs from 'fs';
import { fileURLToPath } from 'url';
import { dirname } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const input = fs.readFileSync(`${__dirname}/input.txt`, 'utf-8')
    .split('\n')
    .map(row => row.split(': ')[1])
    .map(row => row
        .split('; ')
        .map(item => item.split(', ')
            .map(item => item.split(' '))
            .map(item => [item[1], parseInt(item[0])])
        )
        .map(item => new Map(item))
    );

// 12 red cubes, 13 green cubes, and 14 blue cubes
function solution1() {
    let result = 0;

    for (let i = 0; i in input; i++) {
        const game = input[i];

        if (game.some(draw => {
            if (draw.has('red') && draw.get('red') > 12) return true;
            if (draw.has('green') && draw.get('green') > 13) return true;
            if (draw.has('blue') && draw.get('blue') > 14) return true;
            return false;
        })) continue;

        result += i + 1;
    }

    return result;
}

function solution2() {
    let result = 0;

    for (const game of input) {
        let red = 0;
        let green = 0;
        let blue = 0;

        for (const draw of game) {
            if (draw.has('red')) red = Math.max(red, draw.get('red'));
            if (draw.has('green')) green = Math.max(green, draw.get('green'));
            if (draw.has('blue')) blue = Math.max(blue, draw.get('blue'));
        }

        result += red * green * blue;
    }

    return result;
}

console.log(solution1());
console.log(solution2());
