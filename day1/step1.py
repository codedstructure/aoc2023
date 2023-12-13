import re

def lines():
    with open('inputs.txt') as f:
        yield from f

total = 0
for line in lines():
    first_digit = re.search('[0-9]', line)
    last_digit = re.search('[0-9a-z]*([0-9])', line)
    total += int(first_digit.group(0)) * 10 + int(last_digit.group(1))

print(total)
