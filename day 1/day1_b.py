import itertools
f = open('input.txt', "r")
frequency = 0
list = []
seen = {0}
for line in f:
    list.append(int(line))
for num in itertools.cycle(list):
    frequency += num
    if frequency in seen:
        print(frequency);
        break
    seen.add(frequency)