import re

up_asleep = {}

with open('sorted-input.txt') as s:
    current_guard = ''
    current_day = ''

    for entry in s:
        if '#' in entry:
            guard = re.search('#(\w*)', entry)
            current_guard = guard.group(1)
            if not up_asleep.get(current_guard):
                up_asleep.update({
                    current_guard: {}
                })
        else:
            e = re.search('^(\w*-\w*-\w*) \d{2}:(\d{2}), (\w*)', entry)
            day = e.group(1)
            minute = int(e.group(2))
            state = e.group(3)

            if day != current_day:
                current_day = day
                up_asleep[current_guard].update({
                    current_day: [0] * 60
                })
                current_minute = 0
                current_state = 'up'

            if current_state == 'asleep':
                for i in range(current_minute, minute):
                    up_asleep[current_guard][current_day][i] = 1

            current_minute = minute

            if state != current_state:
                current_state = state

max_asleep = 0
max_asleep_min = {
    'index': 0,
    'value': 0,
    'guard': ''
}
for g, days in up_asleep.items():
    sum_asleep = [0] * 60
    for d, minutes in days.items():
        for i, m in enumerate(minutes):
            sum_asleep[i] += m

    up_asleep[g].update({
        'sum_asleep': sum_asleep
    })

    if sum(sum_asleep) > max_asleep:
        max_asleep = sum(sum_asleep)
        asleep_guard = g

    if max(sum_asleep) > max_asleep_min['value']:
        max_asleep_min['value'] = max(sum_asleep)
        max_asleep_min['index'] = sum_asleep.index(max(sum_asleep))
        max_asleep_min['guard'] = g

asleep_guard_minutes_sum = up_asleep[asleep_guard]['sum_asleep']
print('The guard #{} slept the most ({} minutes in total).\n'
      'He slept the most during minute {} ({} times).'
      .format(asleep_guard,
              sum(asleep_guard_minutes_sum),
              asleep_guard_minutes_sum.index(max(asleep_guard_minutes_sum)),
              max(asleep_guard_minutes_sum)))

print('The guard #{} slept more during the minute {} '
      'than any other guard during any other minute ({} times).'
      .format(max_asleep_min['guard'],
              max_asleep_min['index'],
              max_asleep_min['value']))
