def find_div_by_a_or_b(numbers, a, b):
    result = []
    for num in numbers:
        if (num % a == 0) != (num % b == 0):
            result.append(num)
    return result
