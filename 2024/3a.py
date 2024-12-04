import re

with open('3.txt') as f:
    line = f.read()

i = 0
length = len(line)
# pattern = re.compile(r'mul\(\d{1,3},\d{1,3}\)')
pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')

sum = 0

while i < length:
    if line[i:i+4] == 'mul(':
        match = pattern.match(line, i)
        if match:
            i = match.end()
            num1 = match.group(1)
            num2 = match.group(2)
            sum += int(num1) * int(num2)
        else:
            i += 1
    else:
        i += 1

print(sum)