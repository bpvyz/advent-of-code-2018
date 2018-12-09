from collections import Counter, defaultdict
with open('input_sorted.txt', 'r') as f:
    data = [line.strip() for line in f.readlines()]
guards = Counter()
times = defaultdict(list)
for line in data:
    word = line.split(', ')
    print(word)
    mon, day, hour, minute = word[0].split(','), word[1].split(','), word[2].split(','), word[3].split(',')
    mon, day, hour, minute = int(mon[0]), int(day[0]), int(hour[0]), int(minute[0])
    if '#' in word[4]:
        guard = int((((word[4].split())[1]).split('#'))[1])
        if guard not in guards:
            guards[guard]=0
            times[guard]=[]
    elif 'falls' in word[4]:
        start = minute
    elif 'wakes' in word[4]:
        end = minute
        guards[guard]+=end-start
        for i in range(start,end):
            times[guard].append(i)
print("FORMAT: [(ID, MINUTES SLEPT)]: ",guards.most_common())
data = Counter(times.get(guards.most_common(1)[0][0]))
print("MOST COMMON MINUTE: ",data.most_common())



