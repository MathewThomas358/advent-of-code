with open('6.txt') as f:
    lines = [list(line.strip()) for line in f]

current_pos = (0, 0)

def is_within_bounds(pos):
    return 0 <= pos[0] < len(lines) and 0 <= pos[1] < len(lines[0])

current_direction = (-1, 0)

def switch_direction(direction):
    global current_direction
    if direction == (-1, 0):
        current_direction = (0, 1)
    elif direction == (0, 1):
        current_direction = (1, 0)
    elif direction == (1, 0):
        current_direction = (0, -1)
    elif direction == (0, -1):
        current_direction = (-1, 0)

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == '^':
            current_pos = (i, j)

count = 0

while is_within_bounds(current_pos):

    if lines[current_pos[0]][current_pos[1]] == '.' or lines[current_pos[0]][current_pos[1]] == '^':
        count += 1  
        lines[current_pos[0]][current_pos[1]] = 'X'

    if is_within_bounds((current_pos[0] + current_direction[0], current_pos[1] + current_direction[1])) and lines[current_pos[0] + current_direction[0]][current_pos[1] + current_direction[1]] == '#':
        switch_direction(current_direction)
    
    current_pos = (current_pos[0] + current_direction[0], current_pos[1] + current_direction[1])   

print(count)
