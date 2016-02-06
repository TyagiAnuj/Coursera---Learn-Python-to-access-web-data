import re
x = open('regex_sum_238649.txt')
sum = 0
for line in x:
    line = line.rstrip()
    x = re.findall('[0-9]+', line)
    if len(x) > 0:
        for item in x:
            sum += int(item)

print sum
