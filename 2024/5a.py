ordering_rules = []
updates = []

ordering_rules_dict = {}


with open('5.txt') as f:
    for line in f:
        if line == '\n':
            break
        num1, num2 = line.strip().split("|")
        if num1 not in ordering_rules_dict:
            ordering_rules_dict[num1] = set()
        ordering_rules_dict[num1].add(num2)
    for line in f:
        updates.append(line.strip().split(","))

sum = 0

for update in updates:
    flag = True
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            if update[j] not in ordering_rules_dict:
                continue
            if update[i] in ordering_rules_dict[update[j]]:
                flag = False
                break
    if flag:
        sum += int(update[int((len(update) - 1)/2)])
print(sum)