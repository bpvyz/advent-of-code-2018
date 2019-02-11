dots = []
with open('input.txt', 'r') as f:
    for line in f:
        words = line.split('<')
        posxy = words[1].split(',')
        x, y = posxy[0].strip(), posxy[1].split('>')[0].strip()
        xy = words[2].split(',')
        vx, vy = xy[0].strip(), xy[1].split('>')[0].strip()
        dot = {'x': int(x), 'y': int(y), 'vx': int(vx), 'vy': int(vy)}
        dots.append(dot)

t = 0
while True:
    xmin, ymin = 1000000, 1000000
    xmax, ymax = -1000000, -1000000
    for dot in dots:
        dot['x'] = dot['x'] + dot['vx']
        dot['y'] = dot['y'] + dot['vy']
        if xmin > dot['x']:
            xmin = dot['x']
        if xmax < dot['x']:
            xmax = dot['x']
        if ymin > dot['y']:
            ymin = dot['y']
        if ymax < dot['y']:
            ymax = dot['y']
    area = (ymax - ymin) * (xmax - xmin)
    t += 1
    if area == 549:
        break
print(xmin, xmax, ymin, ymax)
matrix = [[' ' for x in range(xmin, xmax+1)] for y in range(ymin, ymax+1)]


for dot in dots:
    print(dot['x'], dot['y'])
    print(len(matrix), len(matrix[0]))
    matrix[dot['y'] - ymin][dot['x'] - xmin] = 'x'
for line in matrix:
    print(''.join(line))
print(t)