from collections import Counter, defaultdict
with open('input_sorted.txt', 'r') as f:
    data = [line.strip() for line in f.readlines()]
guards = defaultdict(Counter)
times = defaultdict(int)
for line in data:
    word = line.split(', ')
    mon, day, hour, minute = word[0].split(','), word[1].split(','), word[2].split(','), word[3].split(',')
    mon, day, hour, minute = int(mon[0]), int(day[0]), int(hour[0]), int(minute[0])
    if '#' in word[5]:
        guard = ((word[5]).split('#')[1])[:-1]
    elif 'falls' in word[4]:
        start = minute
    elif 'wakes' in word[4]:
        end = minute
        for x in range(start, end):
            guards[id].x)
        times[id] += end-start
print (guards)