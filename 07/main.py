import re
import json

dependencies = {}

with open('input.txt', 'r') as dep:
    for l in dep:
        steps = re.search(' ([A-Z]).* ([A-Z])', l)
        step = steps.group(2)
        dep = steps.group(1)

        if not dependencies.get(step):
            dependencies.update({
                step: []
            })

        dependencies[step].append(dep)

no_dep = {}
for step, dep in dependencies.items():
    for d in dep:
        if not dependencies.get(d):
            no_dep.update({d: []})
dependencies.update(no_dep)


def compute_order():
    available = ''
    available += ''.join([s for s, d in dependencies.items() if not d])

    done = []
    to_check = []
    while available:
        to_do = min(available)
        done.append(to_do)
        available = available.replace(to_do, '')

        for s, d in dependencies.items():
            if to_do in d and s not in to_check:
                to_check.append(s)

        new_available = []
        for s in to_check:
            deps = dependencies.get(s)
            done_deps = 0
            for d in deps:
                if d in done:
                    done_deps += 1
            if done_deps == len(deps) and s not in available:
                new_available.append(s)

        for a in new_available:
            to_check.pop(to_check.index(a))
            available += a

    print('Steps order: %s' % ''.join(done))


def compute_order_durations(n_workers):
    available = ''
    available += ''.join([s for s, d in dependencies.items() if not d])

    done = []
    to_check = []
    workers = [''] * n_workers
    workers_occupation = [0] * n_workers
    total_duration = 0
    while len(done) < len(dependencies):
        attributed = False
        total_duration += 1
        done_now = []

        for i, w in enumerate(workers):
            to_do = ''
            if available:
                to_do = min(available)
            if not w and to_do and not attributed:
                workers[i] = to_do
                workers_occupation[i] += ord(to_do) - 4
                available = available.replace(to_do, '')
                attributed = True
            if workers_occupation[i] > 0:
                workers_occupation[i] -= 1
                if workers_occupation[i] == 0:
                    done.append(w)
                    workers[i] = ''
                    done_now.append(w)

        for s, d in dependencies.items():
            for done_step in done_now:
                if done_step in d and s not in to_check:
                    to_check.append(s)

        new_available = []
        for s in to_check:
            deps = dependencies.get(s)
            done_deps = 0
            for d in deps:
                if d in done:
                    done_deps += 1
            if done_deps == len(deps) and s not in available:
                new_available.append(s)

        for a in new_available:
            to_check.pop(to_check.index(a))
            available += a

        for i, w in enumerate(workers):
            to_do = ''
            if available:
                to_do = min(available)
            if not w and to_do and not attributed:
                workers[i] = to_do
                workers_occupation[i] += ord(to_do) - 4
                available = available.replace(to_do, '')
                attributed = True

    print('Steps order with durations: {}\nTotal duration: {}'
          .format(''.join(done), total_duration))


if __name__ == '__main__':
    compute_order()
    compute_order_durations(5)
