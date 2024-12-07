with open('7.txt') as f:
    lines = [line.strip().split(": ") for line in f]

def calculate(required_sum, current_sum, current_index, length, nums):

    if current_sum == required_sum and current_index == length:
        return True

    if current_index == length:
        return False

    num = int(nums[current_index])

    return (
        calculate(required_sum, current_sum + num, current_index + 1, length, nums) or 
        calculate(required_sum, current_sum * num, current_index + 1, length, nums)
    )

value = 0

for line in lines:

    line[1] = line[1].split(" ")
    nums = len(line[1])

    if calculate(int(line[0]), 0, 0, nums, line[1]):
        value += int(line[0])

print(value)