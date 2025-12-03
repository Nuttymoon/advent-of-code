import os
from math import floor


STARTING_POSITION = 50


def get_input_lines():
    with open(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")
    ) as input_file:
        return list(filter(None, input_file.read().split("\n")))


def find_best_couple(line):
    best_tens_digit = 0
    best_tens_digit_index = 0
    best_ones_digit = 0

    for d in range(0, len(line) - 1):
        if int(line[d]) > best_tens_digit:
            best_tens_digit = int(line[d])
            best_tens_digit_index = d

    for d in range(best_tens_digit_index + 1, len(line)):
        if int(line[d]) > best_ones_digit:
            best_ones_digit = int(line[d])

    return best_tens_digit * 10 + best_ones_digit


if __name__ == "__main__":
    couples_sum = 0

    for line in get_input_lines():
        best_couple = find_best_couple(list(line))
        couples_sum += best_couple

        print(f"{line} -> {best_couple}")

    print(f"Couples sum: {couples_sum}")
