def add(numbers):
    if not numbers:
        return 0
    numbers = [int(n) for n in numbers.split(',')]

    return sum(numbers)



print(add('1,2,3,4,5'))  # 15