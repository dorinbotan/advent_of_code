import os
import re
dir_path = os.path.dirname(os.path.realpath(__file__))


def solution1(seeds, seeds_to_soil, soil_to_fertilizer, fertilizer_to_water,
              water_to_light, light_to_temperature, temperature_to_humidity,
              humidity_to_location):
    leftmost = float('inf')

    for seed in seeds:
        location = seed

        for mapping in [seeds_to_soil,
                        soil_to_fertilizer,
                        fertilizer_to_water,
                        water_to_light,
                        light_to_temperature,
                        temperature_to_humidity,
                        humidity_to_location]:
            for destination, source, _range in mapping:
                if location >= source and location <= source + _range:
                    location = destination - source + location
                    break

        leftmost = min(leftmost, location)

    return leftmost


def solution2(seeds, seeds_to_soil, soil_to_fertilizer, fertilizer_to_water,
              water_to_light, light_to_temperature, temperature_to_humidity,
              humidity_to_location):
    pass


def parse(template, data):
    pattern = re.compile(f'{template}([\\d \\n]+)')
    match = pattern.search(data).group(1).strip().split('\n')
    return list(map(lambda x: list(map(int, x.split(' '))), match))


with open(f'{dir_path}/input.txt', 'r') as f:
    data = f.read()

    seeds = parse('seeds:', data)[0]
    seeds_to_soil = parse('seed-to-soil map:\n', data)
    soil_to_fertilizer = parse('soil-to-fertilizer map:\n', data)
    fertilizer_to_water = parse('fertilizer-to-water map:\n', data)
    water_to_light = parse('water-to-light map:\n', data)
    light_to_temperature = parse('light-to-temperature map:\n', data)
    temperature_to_humidity = parse('temperature-to-humidity map:\n', data)
    humidity_to_location = parse('humidity-to-location map:\n', data)

    result1 = solution1(seeds, seeds_to_soil, soil_to_fertilizer,
                        fertilizer_to_water, water_to_light, light_to_temperature,
                        temperature_to_humidity, humidity_to_location)
    print(result1)

    result2 = solution2(seeds, seeds_to_soil, soil_to_fertilizer,
                        fertilizer_to_water, water_to_light, light_to_temperature,
                        temperature_to_humidity, humidity_to_location)
    print(result2)
