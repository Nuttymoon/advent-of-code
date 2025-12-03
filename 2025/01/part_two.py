import os
from math import floor


STARTING_POSITION = 50


def get_input_lines():
    with open(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")
    ) as input_file:
        return list(filter(None, input_file.read().split("\n")))


def read_rotation(rotation):
    direction = 1 if rotation[0] == "R" else -1
    distance = int(rotation[1:])

    return direction, distance


if __name__ == "__main__":
    position = STARTING_POSITION
    zero_crossings = 0

    for r in get_input_lines():
        direction, distance = read_rotation(r)

        # Brute force, but it works.
        for _ in range(0, distance):
            position = (position + direction) % 100
            if position == 0:
                zero_crossings += 1

        print(f"{r} -> {position}")

    print(f"Zero crossings (= door password): {zero_crossings}")
