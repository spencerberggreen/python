import random
import time
import copy
width = 60
height = 20

next_cells = []
for x in range(width):
    column = []
    for y in range(height):
        if random.randint(0, 1) == 0:
            column.append('#')
        else:
            column.append(' ')
    next_cells.append(column)

while True:
    print('\n\n\n\n\n')
    current_cells = copy.deepcopy(next_cells)
    for y in range(height):
        for x in range(width):
            print(current_cells[x][y], end='')
        print()
    for x in range(width):
        for y in range(height):
            left_coord = (x - 1) % width
            right_coord = (x + 1) % width
            above_coord = (y - 1) % height
            below_coord = (y + 1) % height

            num_neighbors = 0
            if current_cells[left_coord][above_coord] == '#':
                num_neighbors += 1
            if current_cells[x][above_coord] == '#':
                num_neighbors += 1
            if current_cells[right_coord][above_coord] == '#':
                num_neighbors += 1
            if current_cells[left_coord][y] == '#':
                num_neighbors += 1
            if current_cells[right_coord][y] == '#':
                num_neighbors += 1
            if current_cells[left_coord][below_coord] == '#':
                num_neighbors += 1
            if current_cells[x][below_coord] == '#':
                num_neighbors += 1
            if current_cells[right_coord][below_coord] == '#':
                num_neighbors += 1

            if current_cells[x][y] == '#' and (num_neighbors == 2 or num_neighbors == 3):
                next_cells[x][y] = '#'
            elif current_cells[x][y] == ' ' and num_neighbors == 3:
                next_cells[x][y] = '#'
            else:
                next_cells[x][y] = ' '
    time.sleep(.5)
