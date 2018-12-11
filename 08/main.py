import json

headers = []

with open('input.txt', 'r') as headers_file:
    headers.extend(headers_file.read().split(' '))

headers = [int(h) for h in headers]
metadata_sum = 0


def parse_node(header):
    global metadata_sum

    nb_childs = header.pop(0)
    nb_metadata = header.pop(0)
    childs = []
    metadata = []
    value = 0

    for _ in range(0, nb_childs):
        childs.append(parse_node(header))

    for _ in range(0, nb_metadata):
        metadata.append(header.pop(0))

    if childs:
        for m in metadata:
            if m <= len(childs):
                value += childs[m - 1]['value']
    else:
        value = sum(metadata)

    metadata_sum += sum(metadata)
    return {
        'nb_childs': nb_childs,
        'childs': childs,
        'nb_metadata': nb_metadata,
        'metadata': metadata,
        'value': value
    }


if __name__ == '__main__':
    master_node = parse_node(headers)
    print('Metada entries sum: {}\nRoot node value: {}'
          .format(metadata_sum, master_node['value']))
