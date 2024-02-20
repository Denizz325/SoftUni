def calculate_the_factorial(number):
    for current_number in range(1, number):
        number *= current_number
    return number


first_number = int(input())
second_number = int(input())

first_numbers_factorial = calculate_the_factorial(first_number)
second_numbers_factorial = calculate_the_factorial(second_number)

result = first_numbers_factorial / second_numbers_factorial

print(f"{result:.2f}")