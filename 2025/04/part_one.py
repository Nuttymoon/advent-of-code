import os
from math import floor


def get_input_lines():
    with open(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")
    ) as input_file:
        return list(filter(None, input_file.read().split("\n")))


def lines_to_matrix(lines):
    return [list(row) for row in lines]


def count_adjacent_rolls(position, matrix):
    rolls = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if position[0] + i in [-1, len(matrix)] or position[1] + j in [
                -1,
                len(matrix[0]),
            ]:
                continue
            if i == 0 and j == 0:
                continue
            if matrix[position[0] + i][position[1] + j] == "@":
                rolls += 1
    return rolls


if __name__ == "__main__":
    matrix = lines_to_matrix(get_input_lines())
    accessible_rolls = 0

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if matrix[i][j] == "@":
                rolls = count_adjacent_rolls((i, j), matrix)
                print(f"({i}, {j}) -> {rolls}")

                if rolls < 4:
                    accessible_rolls += 1

    print(f"Accessible rolls: {accessible_rolls}")
