import re

entries = {}

with open('input.txt', 'r') as entries_file:
    for entry in entries_file:
        if '#' in entry:
            e = re.search('\[(.*)\] \w* (#\w*)', entry)
        else:
            e = re.search('\[(.*)\] \w* (\w*)', entry)

        entries.update({
            e.group(1): e.group(2)
        })

with open('sorted-input.txt', 'w') as sorted_entries:
    for e in sorted(entries.items()):
        sorted_entries.write('{}, {}\n'.format(e[0], e[1]))
