import numpy

box_ids = []
two_times = 0
three_times = 0

with open('input.txt', 'r') as boxes:
    box_ids = boxes.read().splitlines()

letters_count = numpy.zeros((len(box_ids), 26))

for i, b in enumerate(box_ids):
    for letter in b:
        letters_count[i][ord(letter) - 97] += 1

for l_count in letters_count:
    if 2 in l_count:
        two_times += 1
    if 3 in l_count:
        three_times += 1

print('Number of letters appearing two times: {}\n'
      'Number of letters appearing three times: {}\n'
      'Checksum: {}'.format(two_times, three_times, two_times*three_times))

similar_boxes = []

letters_count_cp = list(letters_count)
removed = 0

print('Similar box couples:\n')

for index1, b1 in enumerate(letters_count):
    letters_count_cp.pop(0)
    removed += 1
    for index2, b2 in enumerate(letters_count_cp):
        if len([i for i, j in zip(b1, b2) if i == j]) >= 24 \
                and len([i for i, j in zip(b1, b2) if i == j]) < 26:
            similar_boxes.append((box_ids[index1], box_ids[index2 + removed]))
            print('\n'.join([box_ids[index1], box_ids[index2 + removed], ' ']))

for box_couple in similar_boxes:
    common_letters = []
    diff_count = 0

    for i, letter in enumerate(box_couple[0]):
        if letter == box_couple[1][i]:
            common_letters += letter
        else:
            diff_count += 1

    if diff_count == 1:
        print('Target boxes ids:\n{}\n{}\n\nCommon letters: {}\n'
              .format(box_couple[0], box_couple[1],
                      ''.join(common_letters)))
