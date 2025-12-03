import os
from math import floor


STARTING_POSITION = 50


def get_input_lines():
    with open(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")
    ) as input_file:
        return list(filter(None, input_file.read().split("\n")))


def read_rotation(rotation):
    direction = rotation[0]
    distance = int(rotation[1:])

    if direction == "L":
        return distance * -1

    return distance


def rotate(starting_position, distance):
    return (starting_position + distance) % 100


if __name__ == "__main__":
    position = STARTING_POSITION
    zero_crossings = 0

    for r in get_input_lines():
        position = rotate(position, read_rotation(r))
        if position == 0:
            zero_crossings += 1

        print(f"{r} -> {position}")

    print(f"Zero crossings (= door password): {zero_crossings}")
