with open('2.txt') as f:
    data = f.read().split('\n')

reports = []
for line in data:
    reports.append([int(x) for x in line.split(' ')])

def safe(report):
    if report != sorted(report) and report != sorted(report)[::-1]:
        return False
    for i  in range(len(report)-1):
        if abs(report[i]-report[i+1]) <1 or  abs(report[i]-report[i+1])>3:
            return False
    return True 

def safe_2(report):
    if safe(report):
        return True
    for i in range(len(report)):
        temp_report = report[:i] + report[i+1:]
        if safe(temp_report):
            return True
    return False

answer = sum([1 for report in reports if safe_2(report) ])
print(f'answer to part 2 is {answer}')