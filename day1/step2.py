
import re

def lines():
    with open('inputs.txt') as f:
        yield from f

def convert(digit):
    if digit[0].isdigit():
        return int(digit)
    return {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7, 
        'eight': 8,
        'nine': 9,
        'zero': 0,
    }[digit]

total = 0
for line in lines():

    first_digit = re.search('(one|two|three|four|five|six|seven|eight|nine|[0-9])', line)
    last_digit = re.search('[0-9a-z]*(one|two|three|four|five|six|seven|eight|nine|[0-9])', line)
    first_digit = first_digit.group(0)
    last_digit = last_digit.group(1)

    total += convert(first_digit) * 10 + convert(last_digit)

print(total)
