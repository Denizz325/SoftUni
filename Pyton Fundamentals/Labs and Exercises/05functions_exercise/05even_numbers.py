number_as_str = input().split()
number_as_digits = []

for numbers in number_as_str:
    number_as_digits.append(int(numbers))

is_even = lambda x: x % 2 == 0

result = list(filter(is_even,number_as_digits))

print(result)