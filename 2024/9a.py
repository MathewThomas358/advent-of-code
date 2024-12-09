with open('9.txt') as f:
    disk_map = f.readline().strip()

disk_map_expanded = []
disk_map_defrag = []

disk_id = 0
total_blocks = 0

for i in range(len(disk_map)):
    if i % 2 == 0:
        for j in range(int(disk_map[i])):
            disk_map_expanded.append(disk_id)
            disk_map_defrag.append(disk_id)
            total_blocks += 1
        disk_id += 1
    else:
        for j in range(int(disk_map[i])):
            disk_map_expanded.append('.')

for i in range(len(disk_map_expanded)):
    if disk_map_expanded[i] == '.':
        disk_map_expanded[i] = disk_map_defrag.pop(len(disk_map_defrag) - 1)
    

checksum = 0

for i in range(total_blocks):
    checksum += disk_map_expanded[i] * i

print(checksum)