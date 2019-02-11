f = open("input_sorted.txt", "w+")
for line in open('input.txt', 'r'):
    words = line.split('<')
    posxy = words[1].split(',')
    posx, posy = posxy[0].strip(), posxy[1].split('>')[0].strip()
    velxy = words[2].split(',')
    velx, vely = velxy[0].strip(), velxy[1].split('>')[0].strip()
    print(posx, posy, velx, vely)
    f.write(posx + ',' + posy + ',' + velx + ',' + vely + '\n')