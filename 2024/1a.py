with open('1a.txt') as f:
    lines = f.readlines()

list1 = []
list2 = []

for line in lines:
    line = line.strip().split()
    list1.append(int(line[0]))
    list2.append(int(line[1]))

list1 = sorted(list1)
list2 = sorted(list2)

sum = 0

for i in range(len(list1)):
    sum += abs(list1[i] - list2[i])

print(sum)