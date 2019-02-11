serial = 9424
matrix = [[(x, y) for x in range(300)] for y in range(300)]
matrix_of_powerlevels = []

for line in matrix:
    for cell in line:
        rack_id = cell[0] + 10
        power_level = rack_id * cell[1]
        matrix_of_powerlevels.append((((power_level+serial)*rack_id) // 100) % 10 - 5)
print(matrix_of_powerlevels[:-602])