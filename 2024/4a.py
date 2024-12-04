with open('4.txt') as f:
    lines = [line.strip() for line in f]

matrix = [list(line) for line in lines]
word = "XMAS"

def find_all_occurrences(matrix, word):
    rows = len(matrix)
    cols = len(matrix[0])
    word_len = len(word)
    count = 0

    directions = [
        (0, 1),  
        (1, 0), 
        (1, 1),
        (-1, 1),
        (0, -1),
        (-1, 0),
        (-1, -1),
        (1, -1) 
    ]

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def search_from(x, y, dx, dy):
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
            if not is_valid(nx, ny) or matrix[nx][ny] != word[i]:
                return False
        return True

    for i in range(rows):
        for j in range(cols):
            for (dx, dy) in directions:
                if search_from(i, j, dx, dy):
                    count += 1

    return count

occurrences = find_all_occurrences(matrix, word)
print(occurrences)