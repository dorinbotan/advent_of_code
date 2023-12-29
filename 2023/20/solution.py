import os

dir_path = os.path.dirname(os.path.realpath(__file__))


class FlipFlop:
    def __init__(self, outputs):
        self.outputs = outputs
        self.value = False

    # when a high pulse is received, nothing happens
    # when a low pulse is received, flip between on and off
    # if it was on, it turns off and sends a low pulse
    # If it was off, it turns on and sends a high pulse
    def trigger(self, _, value):
        if value:
            return None, None

        self.value = not self.value

        return self.value, self.outputs


class Conjunction:
    def __init__(self, outputs, inputs):
        self.outputs = outputs
        self.values = dict()
        for input in inputs:
            self.values[input] = False

    # when a pulse is received, first update memory for that input
    # then, if remember high pulses for all inputs, send a low pulse
    # otherwise, send a high pulse
    def trigger(self, input, value):
        self.values[input] = value

        return not all(self.values.values()), self.outputs


class Broadcaster:
    def __init__(self, outputs):
        self.outputs = outputs

    # when a pulse is received, send it to all outputs
    def trigger(self, _, value):
        return value, self.outputs


def parse_modules(modules):
    links = dict()

    for module in modules:
        name, outputs = module.split(' -> ')
        if name != 'broadcaster':
            name = name[1:]

        if name not in links:
            links[name] = {
                'inputs': [],
                'outputs': [],
            }

        links[name]['outputs'] = outputs.split(', ')

        for output in outputs.split(', '):
            if output not in links:
                links[output] = {
                    'inputs': [],
                    'outputs': [],
                }
            links[output]['inputs'].append(name)

    result = dict()

    for module in modules:
        name = module.split(' -> ')[0]

        if name[0] == '%':
            outputs = links[name[1:]]['outputs']
            result[name[1:]] = FlipFlop(outputs)
        elif name[0] == '&':
            inputs = links[name[1:]]['inputs']
            outputs = links[name[1:]]['outputs']
            result[name[1:]] = Conjunction(outputs, inputs)
        else:
            outputs = links[name]['outputs']
            result[name] = Broadcaster(outputs)

    return result


def solution1(modules):
    queue = []

    low = 0
    high = 0

    for _ in range(1000):
        queue.append([None, False, 'broadcaster'])

        while queue:
            input, value, module = queue.pop(0)

            if value:
                high += 1
            else:
                low += 1

            # ignore 'rx' and 'output' modules
            if module not in modules:
                continue

            value, outputs = modules[module].trigger(input, value)

            if outputs is None:
                continue

            for output in outputs:
                queue.append([module, value, output])

    return low * high


def solution2(modules):
    pass


with open(f'{dir_path}/input.txt', 'r') as f:
    data = f.read().splitlines()
    modules = parse_modules(data)

    result1 = solution1(modules)  # 929810733
    print(result1)

    result2 = solution2(modules)
    print(result2)
