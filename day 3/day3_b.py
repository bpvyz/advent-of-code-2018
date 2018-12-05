f = open('input.txt', "r")
fabric = [[0 for x in range(1000)] for x in range(1000)]
for line in f:
    words = line.split()
    x, y = words[2].split(',')
    x, y = int(x), int(y[:-1])
    w, h = words[3].split('x')
    w, h = int(w), int(h)
    for row in range(h):
        for col in range(w):
            fabric[y+row][x+col] = fabric[y+row][x+col]+1
f.seek(0)
for line in f:
    words = line.split()
    x, y = words[2].split(',')
    x, y = int(x), int(y[:-1])
    w, h = words[3].split('x')
    w, h = int(w), int(h)
    overlap = False
    for row in range(h):
        for col in range(w):
            if fabric[y+row][x+col] >= 2:
                overlap = True
                break
        if overlap is True:
            break
    if overlap is False:
        print(line)