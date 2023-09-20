number = int(input())

for current_number in range(1, number):
    current_number_as_str = str(current_number)
    digit_sum = 0

    for digit in current_number_as_str:
        digit_sum += int(digit)

    is_special = False

    if digit_sum == 5 or digit_sum == 7 or digit_sum == 11:
        is_special = True
    print(f"{current_number} -> {is_special}")