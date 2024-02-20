def min_numbers(some_numbers: int) -> int:
    return min(some_numbers)


def max_number(some_number: int) -> int:
    return max(some_number)


def sum_numbers(some_number: int) -> int:
    return sum(numbers)


numbers = list(map(int, input().split()))

print(f"The minimum number is {min_numbers(numbers)}")
print(f"The maximum number is {max_number(numbers)}")
print(f"The sum number is: {sum_numbers(numbers)}")