import re
import numpy as np


def print_result(output_file, points):
    min_x = min([p['x'] for p in points])
    max_x = max([p['x'] for p in points])
    min_y = min([p['y'] for p in points])
    max_y = max([p['y'] for p in points])
    sky = np.zeros((max_x + abs(min_x), max_y + abs(min_y)))

    for p in points:
        p['x'] += abs(min_x)
        p['y'] += abs(min_y)
        sky[p['x'] - 1][p['y'] - 1] = 1

    with open(output_file, 'w+') as out:
        for l in sky:
            out.write(''.join([' ' if p == 0 else '#' for p in l]) + '\n')


points = []
positions = []

with open('input.txt', 'r') as points_file:
    for p in points_file:
        s = re.search('< ?(-?\d+),  ?(-?\d+)>.*< ?(-?\d+),  ?(-?\d+)>', p)
        points.append({
            'x': int(s.group(1)),
            'y': int(s.group(2)),
            'x_velocity': int(s.group(3)),
            'y_velocity': int(s.group(4))
        })

it = 0
scatter = max([p['x'] for p in points]) - min([p['x'] for p in points])
stop = False
while not stop:
    if not it % 100:
        print(it, scatter)

    previous_points = list(points)

    for i, p in enumerate(points):
        p['x'] += p['x_velocity']
        p['y'] += p['y_velocity']

    scatter2 = max([p['x'] for p in points]) - min([p['x'] for p in points])

    if scatter2 >= scatter:
        stop = True
    else:
        scatter = scatter2

    it += 1

around_intersect = []
previous_points = list(points)
next_points = list(points)
print_result('output.txt', points)
for index in range(0, 2):
    for i, p in enumerate(previous_points):
        p['x'] += p['x_velocity']
        p['y'] += p['y_velocity']

    for i, p in enumerate(next_points):
        p['x'] += p['x_velocity']
        p['y'] += p['y_velocity']

    around_intersect.append(previous_points)
    around_intersect.append(next_points)

    print_result('output-%d.txt' % (index + 1), previous_points)
    print_result('output+%d.txt' % (index + 1), next_points)
