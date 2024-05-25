import re

def add(numbers):
    if not numbers:
        return 0
    
    #habdle new lines and custom delimiters
    if numbers.startswith('//'):
        delimiter, numbers = numbers.split('\n', 1)
        delimiter = delimiter[2:]
        numbers = re.split(re.escape(delimiter) + r'|\n', numbers)
    else:
        numbers = re.split(r',|\n', numbers)
    
    numbers = list(map(int, numbers))

    #check for negative numbers
    if any(n < 0 for n in numbers):
        raise ValueError('Negatives not allowed')

    return sum(numbers)

# Path: test_calc.py