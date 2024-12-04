with open('4.txt') as f:
    lines = [line.strip() for line in f]

matrix = [list(line) for line in lines]
word1 = "MAS"
word2 = "SAM"

def find_x_mas(matrix, word1, word2):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def check_forward_diagonal(x, y, word):
        for i in range(len(word)):
            nx, ny = x + i, y + i
            if not is_valid(nx, ny) or matrix[nx][ny] != word[i]:
                return False
        return True

    def check_reverse_diagonal(x, y, word):
        for i in range(len(word)):
            nx, ny = x + i, y - i
            if not is_valid(nx, ny) or matrix[nx][ny] != word[i]:
                return False
        return True

    for i in range(rows):
        for j in range(cols):
            if check_forward_diagonal(i, j, word1) or check_forward_diagonal(i, j, word2):
                if is_valid(i, j + 2):
                    if check_reverse_diagonal(i, j + 2, word1) or check_reverse_diagonal(i, j + 2, word2):
                        count += 1

    return count

occurrences = find_x_mas(matrix, word1, word2)
print(occurrences)
