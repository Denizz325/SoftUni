def positive_num(list_of_nums):
    return ', '.join([number for number in numbers if int(number) >= 0])


def negative_num(list_of_nums):
    return ', '.join([number for number in numbers if int(number) < 0])


def even_num(list_of_nums):
    return ', '.join([number for number in numbers if int(number) % 2 == 0])


def odd_num(list_of_nums):
    return ', '.join([number for number in numbers if int(number) % 2 != 0])


numbers = input().split(", ")

print(f"Positive: {positive_num(numbers)}")
print(f"Negative: {negative_num(numbers)}")
print(f"Even: {even_num(numbers)}")
print(f"Odd: {odd_num(numbers)}")
