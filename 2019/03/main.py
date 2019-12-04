import os
from math import floor


def get_input_lines():
    with open(os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            'input.txt')) as input_file:
        return list(filter(None, input_file.read().split('\n')))


def operate_move(direction):
    return {
        'R': lambda x: (x[0] + 1, x[1]),
        'L': lambda x: (x[0] - 1, x[1]),
        'U': lambda x: (x[0], x[1] + 1),
        'D': lambda x: (x[0], x[1] - 1)
    }.get(direction)


def generate_path(path_sections):
    path = []
    current_pos = (0, 0)

    for move in list(filter(None, path_sections.split(','))):
        direction = move[0]
        distance = int(move[1:])

        for _ in range(0, distance):
            current_pos = operate_move(direction)(current_pos)

            path.append(current_pos)

    return path


def get_intersections(path1, path2):
    return list(set(path1) & set(path2))


def manhattan_distance(coordinates):
    return abs(coordinates[0]) + abs(coordinates[1])


def order_by_manhattan(points):
    ordered = []

    for p in points:
        ordered.append((manhattan_distance(p), p))

    return sorted(ordered)


def order_by_combined_steps(points, path1, path2):
    ordered = []

    for p in points:
        ordered.append((path1.index(p) + path2.index(p) + 2, p))

    return sorted(ordered)


if __name__ == '__main__':
    paths = []

    for wire_sections in get_input_lines():
        paths.append(generate_path(wire_sections))

    print(
        'Manhattan distance of the insersection closest to the central port =',
        order_by_manhattan(get_intersections(paths[0], paths[1]))[0][0])

    print(
        'Fewest combined steps to reach an intersection = ',
        order_by_combined_steps(get_intersections(paths[0], paths[1]),
                                paths[0], paths[1])[0][0])
