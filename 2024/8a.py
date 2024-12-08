with open('8.txt') as f:
    lines = [line.strip() for line in f]

locations = {}

def is_within_bounds(x, y):
    return 0 <= x < len(lines) and 0 <= y < len(lines[0])

def calculate_distance(x1, x2):
    return (x1[0] - x2[0], x1[1] - x2[1])

def find_antinode(x, y):
    dx, dy = calculate_distance(x, y)
    an1, an2 = None, None

    if is_within_bounds(x[0] + dx, x[1] + dy):
        an1 = (x[0] + dx, x[1] + dy)

    if is_within_bounds(y[0] - dx, y[1] - dy):
        an2 = (y[0] - dx, y[1] - dy)

    return an1, an2

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
            an1, an2 = find_antinode(x, y)
            if an1: result.add(an1)
            if an2: result.add(an2)


print(len(result))