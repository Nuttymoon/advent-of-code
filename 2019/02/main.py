import os
from math import floor


def get_op(opcode):
    return {
        1: sum,
        2: lambda a: a[0] * a[1]
    }.get(opcode)


def get_input_lines():
    with open(os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            'input.txt')) as input_file:
        return list(filter(None, input_file.read().split('\n')))


def generate_program(input_text, noun, verb):
    program = [int(x) for x in filter(None, input_text.split(','))]
    program[1] = noun
    program[2] = verb

    return program


def run_program(program):
    op_index = 0

    while True:
        opcode = program[op_index]

        if opcode == 99:
            break

        operands = (program[program[op_index + 1]],
                    program[program[op_index + 2]])
        output_pos = program[op_index + 3]

        program[output_pos] = get_op(opcode)(operands)

        op_index += 4

    return program


def find_noun_verb(input_text, output):
    for noun in range(0, 100):
        for verb in range(0, 100):
            program = generate_program(input_text, noun, verb)

            if run_program(program)[0] == output:
                return noun, verb


if __name__ == '__main__':
    total_fuel_req = 0

    print('Final program (noun=12, verb=2):\n%s\n' %
          run_program(generate_program(get_input_lines()[0], 12, 2)))

    print('Noun and verb to obtain 19690720: noun={}, verb={}'
          .format(*find_noun_verb(get_input_lines()[0], 19690720)))
