ordering_rules = []
updates = []

ordering_rules_dict = {}
wrong_updates = []

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
k = 0

while k < len(updates):
    flag = True
    redo = False
    update = updates[k]
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            if update[j] not in ordering_rules_dict:
                continue
            if update[i] in ordering_rules_dict[update[j]]:
                flag = False
                redo = True
                update[i], update[j] = update[j], update[i]


    if redo:
        k -= 1

    if not flag:
        sum += int(update[int((len(update) - 1)/2)])
    k += 1
    # else:
        # wrong_updates.append(update)
print(sum)

