with open('9.txt') as f:
    disk_map = f.readline().strip()

disk_map_expanded = []

for i,d in enumerate(disk_map):
    if i%2:
        disk_map_expanded.append((None, int(d)))
    else:
        disk_map_expanded.append((i // 2, int(d)))

        
for i in range(len(disk_map_expanded)-1,-1,-1):
    for j in range(i):
        ldata, lsize = disk_map_expanded[i]
        rdata, rsize = disk_map_expanded[j]

        if ldata != None and rdata == None and lsize <= rsize:
            disk_map_expanded[i] = (None, lsize)
            disk_map_expanded[j] = (None, rsize - lsize)
            disk_map_expanded.insert(j, (ldata, lsize))

expanded_list = []
for thing in disk_map_expanded:
    data, size = thing
    if data == None:
        expanded_list.append([0] * size)
    else:
        expanded_list.append([data] * size)

disk_map_expanded = expanded_list

flattened_list = []
for sublist in disk_map_expanded:
    for item in sublist:
        flattened_list.append(item)

result = 0
for i, c in enumerate(flattened_list):
    if c:
        result += i * c

print(result)