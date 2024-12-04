with open('1a.txt') as f:
    lines = f.readlines()

list1 = []
list2 = []

for line in lines:
    line = line.strip().split()
    list1.append(int(line[0]))
    list2.append(int(line[1]))

similarity_score = 0
dict2 = {}

for num in list2:
    if num in dict2:
        dict2[num] += 1
    else:
        dict2[num] = 1

for num in list1:
    if num in dict2:
        similarity_score += num * dict2[num]

print(similarity_score)