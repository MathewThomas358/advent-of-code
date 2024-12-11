with open('11.txt') as f:
    line = f.readline().strip().split(' ')

iterations = 25

def process_num(value):
    nums = [value]

    for _ in range(iterations):
        for i in range(len(nums)):
            if nums[i] == '0':
                nums[i] = '1'

            elif len(nums[i]) % 2 == 0:
                num1 = str(int(nums[i][:len(nums[i])//2]))
                num2 = str(int(nums[i][len(nums[i])//2:]))
                nums[i] = num1
                nums.append(num2)

            else:
                nums[i] = str(int(nums[i]) * 2024)

    return len(nums)

count = 0

for num in line:
    count += process_num(num)

print(count)