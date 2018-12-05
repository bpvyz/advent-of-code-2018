f = open('input.txt', "r")
data = []
differ = 0
for line in f:
    data.append(line.rstrip())
print(len(data))
for id1 in range(0, len(data)-1):
    for id2 in range(id1+1, len(data)):
        differ = 0
        for char1, char2 in zip(data[id1], data[id2]):
            if char1 == char2:
                continue
            else:
                differ += 1
        if differ <= 1:
            data=[data[id1],data[id2]]
            break
    if len(data)==2:
        break
print(data)