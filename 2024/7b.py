with open('7.txt') as f:
    lines = [line.strip().split(": ") for line in f]

def calculate(required_sum, current_sum, current_index, length, nums, allow_concat):

    if current_sum == required_sum and current_index == length:
        return True

    if current_index == length:
        return False

    num = int(nums[current_index])

    return (
        calculate(required_sum, current_sum + num, current_index + 1, length, nums, allow_concat) or
        calculate(required_sum, current_sum * num, current_index + 1, length, nums, allow_concat) or
        (allow_concat and calculate(required_sum, int(str(current_sum) + nums[current_index]), current_index + 1, length, nums, allow_concat))
    )

value = 0

for line in lines:

    nums = line[1].split(" ")
    length = len(nums)

    if calculate(int(line[0]), int(nums[0]), 1, length, nums, False):
        value += int(line[0])

print(value)
