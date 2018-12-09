from collections import defaultdict

xcoordinates=[]
ycoordinates=[]
closest = {}

with open("input.txt") as f:
    data = [line.strip() for line in f.readlines()]

for line in data:
    x,y = line.split(',')
    x,y = int(x), int(y)
    closest[(x,y)]=0
    xcoordinates.append(x)
    ycoordinates.append(y)
xlo = min([x for x in xcoordinates])
xhi = max([x for x in xcoordinates])
ylo = min([y for y in ycoordinates])
yhi = max([y for y in ycoordinates])


def manhattan(x1,y1):
    distance1 = 1000
    alldistances = []
    for coord in range(len(data)):
        distance2 = abs(x1-xcoordinates[coord])+abs(y1-ycoordinates[coord])
        if distance2 < distance1:
            distance1 = distance2
            alldistances.append(distance1)
    if alldistances.count(distance1) != 1:
        return 0
    a=alldistances.index(distance1)
    closest[data[a]] += 1
    return distance1

print(xlo,xhi,ylo,yhi)
for xcell in range(xlo,xhi):
    for ycell in range(ylo,yhi):
        print(manhattan(xcell,ycell))
print(closest)