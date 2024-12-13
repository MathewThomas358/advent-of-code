with open('13.txt', 'r') as file:
    equations = []
    equation = []
    for line in file:
        line = line.strip()
        if "Button A: " in line:
            x1 = int(line.split("Button A: X+")[1].split(", Y+")[0])
            y1 = int(line.split("Y+")[1])
            equation.append(x1)
            equation.append(y1)
        elif "Button B: " in line:
            x2 = int(line.split("Button B: X+")[1].split(", Y+")[0])
            y2 = int(line.split("Y+")[1])
            equation.append(x2)
            equation.append(y2)
        elif "Prize:" in line:
            xc = int(line.split("Prize: X=")[1].split(", Y=")[0])
            yc = int(line.split("Y=")[1])
            equation.append(xc)
            equation.append(yc)
            equations.append(((equation[0], equation[2], equation[4]), (equation[1], equation[3], equation[5])))
            equation = []
        else:
            continue

def solve_equation(x, y):

    x1, x2, xc = x
    y1, y2, yc = y

    result = []

    for a in range(0, 101):
        b = (xc - x1 * a) / x2
        if y1 * a + y2 * b == yc:
            result.append((a, int(b)))

    required_tokens = []

    for token in result:
        required_tokens.append(token[0] * 3 + token[1] * 1)

    if not required_tokens:
        return 0
    return min(required_tokens)

total = 0

for equation in equations:
    total += solve_equation(equation[0], equation[1])

print(total)
