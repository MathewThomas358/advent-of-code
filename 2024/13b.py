import numpy as np

with open('13.txt', 'r') as file:
    equations = []
    equation = []
    error = 10000000000000
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
            equation.append(xc + error)
            equation.append(yc + error)
            equations.append(((equation[0], equation[2], equation[4]), (equation[1], equation[3], equation[5])))
            equation = []

def solve_equation(x, y):

    x1, x2, xc = x
    y1, y2, yc = y

    A = np.array([[x1, x2], [y1, y2]])
    B = np.array([xc, yc])

    try:
        result = np.linalg.solve(A, B)
        return int(np.round([3,1] @ result)) if all(A@result.round() == B) else 0
    except np.linalg.LinAlgError:
        print("Singular matrix")
        return 0

total = 0

for equation in equations:
    total += solve_equation(equation[0], equation[1])

print(total)
