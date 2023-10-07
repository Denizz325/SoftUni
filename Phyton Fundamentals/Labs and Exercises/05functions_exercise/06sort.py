def sort_numbers(some_numbers: int) -> int:
    return sorted(some_numbers)


numbers = list(map(int, input().split()))

print(sort_numbers(numbers))