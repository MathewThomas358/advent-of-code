with open('8.txt') as f:
    lines = [line.strip() for line in f]

locations = {}

def is_within_bounds(x, y):
    return 0 <= x < len(lines) and 0 <= y < len(lines[0])

def calculate_distance(x1, x2):
    return (x1[0] - x2[0], x1[1] - x2[1])

def find_antinode(x1, x2):
    dx, dy = calculate_distance(x1, x2)
    an = []
    curr = x1

    while is_within_bounds(curr[0] + dx, curr[1] + dy):
        an.append((curr[0] + dx, curr[1] + dy))
        curr = (curr[0] + dx, curr[1] + dy)

    curr = x2

    while is_within_bounds(curr[0] - dx, curr[1] - dy):
        an.append((curr[0] - dx, curr[1] - dy))
        curr = (curr[0] - dx, curr[1] - dy)
    
    an.append(x1)
    an.append(x2)

    return an

for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] != '.':
            if lines[i][j] not in locations:
                locations[lines[i][j]] = []
            locations[lines[i][j]].append((i, j))

result = set()

for key, value in locations.items():
    for i in range(len(value)):
        for j in range(i + 1, len(value)):
            x, y = value[i], value[j]
            an = find_antinode(x, y)
            for node in an:
                result.add(node)

print(len(result))