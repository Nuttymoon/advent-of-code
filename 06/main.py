import re


def manhattan_distance(p1, p2):
    x_dist = abs(p1[0] - p2[0])
    y_dist = abs(p1[1] - p2[1])
    return (x_dist + y_dist)


locations = []
x_coord = []
y_coord = []

with open('input.txt', 'r') as loc:
    for l in loc:
        coord = re.search('(\d*), (\d*)', l)
        locations.append(
            (int(coord.group(1)), int(coord.group(2)))
        )
        x_coord.append(int(coord.group(1)))
        y_coord.append(int(coord.group(2)))

x_max = max(x_coord)
y_max = max(y_coord)

grid = [
    [{
        'closest': None,
        'distance': 10000
    }] * (y_max)
] * (x_max)

closest_grid = []
closest_count = [0] * len(locations)
for x, line in enumerate(grid):
    closest_line = []
    for y, point in enumerate(line):
        man_dist = []
        for l in locations:
            man_dist.append(manhattan_distance((x, y), l))
        closest_loc = man_dist.index(min(man_dist))
        point['closest'] = str(closest_loc)
        point['distance'] = min(man_dist)
        closest_count[closest_loc] += 1
        closest_line.append(closest_loc)
    closest_grid.append(closest_line)

borders_x = list(closest_grid[0])
borders_x.extend(list(closest_grid[-1]))
borders_y = list([r[0] for r in closest_grid])
borders_y.extend(list([r[-1] for r in closest_grid]))
found_largest = False
closest_count_reduce = list(closest_count)
while not found_largest:
    largest = closest_count.index(max(closest_count_reduce))
    if largest in borders_x or largest in borders_y:
        closest_count_reduce.pop(
            closest_count_reduce.index(max(closest_count_reduce)))
    else:
        found_largest = True
        print('Grid size: {} x {} = {}'.format(x_max, y_max, x_max * y_max))
        print('Largest finished area countains %d points' %
              max(closest_count_reduce))


with open('output.txt', 'w+') as out:
    for line in closest_grid:
        out.write(''.join(str(line)) + '\n')
