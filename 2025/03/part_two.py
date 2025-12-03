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


def find_best_number(digits, line):
    best_digit = 0
    best_digit_index = 0
    for d in range(0, len(line) - digits + 1):
        if int(line[d]) > best_digit:
            best_digit = int(line[d])
            best_digit_index = d

    if digits > 1:
        return "{}{}".format(
            best_digit, find_best_number(digits - 1, line[best_digit_index + 1 :])
        )
    else:
        return str(best_digit)


if __name__ == "__main__":
    numbers_sum = 0

    for line in get_input_lines():
        best_number = find_best_number(12, list(line))
        numbers_sum += int(best_number)

        print(f"{line} -> {best_number}")

    print(f"Numbers sum: {numbers_sum}")
