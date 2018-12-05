from collections import Counter
f = open('input.txt', "r")
twotimes = 0
threetimes = 0
for line in f:
    counter = Counter(line.rstrip())
    if 2 in counter.values() and 3 in counter.values():
        twotimes += 1
        threetimes += 1
    elif 3 in counter.values() and 2 not in counter.values():
        threetimes += 1
    elif 2 in counter.values() and 3 not in counter.values():
        twotimes += 1
print(twotimes * threetimes)