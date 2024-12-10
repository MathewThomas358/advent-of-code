with open('10.txt') as f:
    data = [line.strip() for line in f.readlines()]

def is_valid(i, j):
    return 0 <= i < len(data) and 0 <= j < len(data[0])

def traverse(i, j, seen, h = 0):
    if is_valid(i, j) and int(data[i][j]) == h:
        if h < 9:
            count = 0
            count += traverse(i + 1, j, seen, h + 1)
            count += traverse(i - 1, j, seen, h + 1)
            count += traverse(i, j + 1, seen, h + 1)
            count += traverse(i, j - 1, seen, h + 1)
            return count
        seen.add((i, j))
        return 1
    return 0

count = 0
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == '0':
            count += traverse(i, j, set())

print(count)
