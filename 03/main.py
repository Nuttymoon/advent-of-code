import re

claims = {}
fabric = [
    [
        {'claims_nb': 0, 'claims_ids': []} for _ in range(0, 1000)
    ] for _ in range(0, 1000)
]
overlapping = 0
no_overlap = None

with open('input.txt', 'r') as cl:
    for l in cl:
        c = re.search('#(\d*) @ (\d*),(\d*): (\d*)x(\d*)', l)
        claims.update({
            c.group(1): {
                'x': int(c.group(2)),
                'y': int(c.group(3)),
                'width': int(c.group(4)),
                'height': int(c.group(5)),
                'overlapping': False
            }
        })

for c_id, c in claims.items():
    for i in range(0, c['width']):
        for j in range(0, c['height']):
            fabric[c['x'] + i][c['y'] + j]['claims_nb'] += 1
            fabric[c['x'] + i][c['y'] + j]['claims_ids'].append(c_id)

for l in fabric:
    for c in l:
        if c['claims_nb'] > 1:
            overlapping += 1
            for c_id in c['claims_ids']:
                claims[c_id]['overlapping'] = True

for c_id, c in claims.items():
    if not c['overlapping']:
        no_overlap = c_id

print('Overlapping squares: {}\nNon overlapping claim ID: {}'
      .format(overlapping, no_overlap))
