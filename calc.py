def add(numbers):
    if not numbers:
        return 0
    
    numbers = [int(n) for n in numbers.split(',')]

    #check for negative numbers
    if any(n < 0 for n in numbers):
        raise ValueError('Negatives not allowed')

    return sum(numbers)

# Path: test_calc.py