import string


def react_polymer(poly):
    reacted = []
    for c in poly:
        if reacted:
            if abs(ord(reacted[-1]) - ord(c)) == 32:
                reacted.pop()
            else:
                reacted.append(c)
        else:
            reacted.append(c)
    return reacted


with open('input.txt', 'r') as p_file:
    polymer = p_file.readline()

simple_reacted = react_polymer(polymer)
print('Polymer after reaction:\n{}\nPolymer lenght: {}'
      .format(''.join(simple_reacted), len(simple_reacted)))

reacted_improved = []
min_lenght = len(polymer)
min_index = -1
min_char = ''

for lower_unit in string.ascii_lowercase:
    to_remove = (lower_unit, lower_unit.upper())
    p = [unit for unit in polymer if unit not in to_remove]
    r = react_polymer(p)
    reacted_improved.append(r)
    if len(r) < min_lenght:
        min_lenght = len(r)
        min_index = string.ascii_lowercase.index(lower_unit)
        min_char = lower_unit

print('Shortest polymer obtained by removing unit {}:\n{}\nPolymer lenght: {}'
      .format(
          '/'.join([min_char.upper(), min_char]),
          ''.join(reacted_improved[min_index]),
          min_lenght))
