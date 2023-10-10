number = int(input())
digit = int(input())

count = 0

while number > 0:
    remainder = number % 2
    number = int(number / 2)

    if remainder == digit:
        count += 1

print(count)