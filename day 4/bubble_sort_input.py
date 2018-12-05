from collections import Counter, defaultdict
with open('input.txt', 'r') as f:
    data = [line.strip() for line in f.readlines()]
unsorted = []
sorted = []
guards = defaultdict(Counter)
for line in data:
    words = line.split()
    hour, minute = words[1].split(':')
    hour, minute = int(hour), int(minute[:-1])
    year, month, day = words[0].split('-')
    month, day = int(month), int(day)
    message = words[2: ]
    unsorted.append([month, day, hour, minute])
    unsorted.append(message)
for j in range(len(unsorted)):
    swapped = False
    i = 0
    while i < len(unsorted) - 2:
        if unsorted[i][0] > unsorted[i+2][0]:
            unsorted[i], unsorted[i+2] = unsorted[i+2], unsorted[i]
            unsorted[i+1], unsorted[i+3] = unsorted[i+3], unsorted[i+1]
            swapped = True
        if unsorted[i][0] == unsorted[i+2][0] and unsorted[i][1] > unsorted[i+2][1]:
            unsorted[i], unsorted[i+2] = unsorted[i+2], unsorted[i]
            unsorted[i+1], unsorted[i+3] = unsorted[i+3], unsorted[i+1]
        if unsorted[i][2] < unsorted[i+2][2] and unsorted[i][0] == unsorted[i+2][0] and unsorted[i][1] == unsorted[i+2][1]:
            unsorted[i], unsorted[i + 2] = unsorted[i + 2], unsorted[i]
            unsorted[i + 1], unsorted[i + 3] = unsorted[i + 3], unsorted[i + 1]
        if unsorted[i][3] > unsorted[i + 2][3] and unsorted[i][2] == unsorted[i+2][2] and unsorted[i][0] == unsorted[i+2][0] and unsorted[i][1] == unsorted[i+2][1]:
            unsorted[i], unsorted[i + 2] = unsorted[i + 2], unsorted[i]
            unsorted[i + 1], unsorted[i + 3] = unsorted[i + 3], unsorted[i + 1]
        i=i+2
    if swapped == False:
        break
print(unsorted)
f = open("input_sorted.txt", "w+")
elem=0
while elem < len(unsorted) - 1:
    f.write(str(unsorted[elem])[1:-1]+", "+str(unsorted[elem+1])+"\n")
    elem+=2