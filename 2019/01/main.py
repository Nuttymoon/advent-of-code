import os
from math import floor


def get_input_lines():
    with open(os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            'input.txt')) as input_file:
        return list(filter(None, input_file.read().split('\n')))


def compute_fuel_req(mass):
    needed_fuel = floor(mass / 3) - 2

    if needed_fuel > 0:
        return needed_fuel + compute_fuel_req(needed_fuel)
    else:
        return 0


if __name__ == '__main__':
    total_fuel_req = 0

    for m in get_input_lines():
        total_fuel_req += compute_fuel_req(int(m))

    print('Total fuel required:', total_fuel_req)
