with open('11.txt') as f:
    # since the ip is small, else we would have to use the num of each n
    lines = {n : 1 for n in f.readline().strip().split(' ')} 

iterations = 75

def add_to_dict(stone, num, somedict):
    # there is definitely a better way to do this
    if stone not in somedict:
        somedict[stone] = 0
    somedict[stone] += num

def process():

    global lines
    somedict = {}

    for stone, num in lines.items():
        if stone == '0':
            add_to_dict('1', num, somedict)
        elif len(stone) % 2 == 0:
            num1 = int(stone[:len(stone)//2])
            num2 = int(stone[len(stone)//2:])
            add_to_dict(str(num1), num, somedict)
            add_to_dict(str(num2), num, somedict)
        else:
            add_to_dict(str(int(stone) * 2024), num, somedict)

    lines = somedict

count = 0

for _ in range(iterations):
    process()

for num in lines.values():
    count += num

print(count)