import csv


def update_freq(frequency, change):
    value = change[1:]
    operation = {
        '-': frequency - int(value),
        '+': frequency + int(value)
    }
    return operation.get(change[:1])


reached = {}
iteration = 1
current = 0

with open('input.txt', 'r') as freq:
    frequencies = freq.read().splitlines()

while 1:
    if not iteration % 100:
        print('Iteration: %d\n' % iteration)

    for f in frequencies:
        current = update_freq(current, f)
        if not reached.get(current, False):
            reached.update(
                {
                    current: True
                })
        else:
            print('First number reached twice: {}\nIteration nb {}\n'
                  .format(current, iteration))
            exit(0)

    iteration += 1
