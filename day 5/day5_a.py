with open("input.txt") as myfile:
    data = "".join(line.rstrip() for line in myfile)
reaction = True
while reaction:
    for i in range(len(data) - 1):
        a = data[i]
        b = data[i+1]
        if (a.swapcase()==b):
            reaction = True
            break
        else:
            reaction = False
            continue
    if not reaction:
        break
    else:
        data = data[:i] + data[(i+2):]
print(len(data))
output = open("reacted_input.txt", "w+")
output.write(data)