num_of_chars = int(input())

total_sum = 0

for i in range(num_of_chars):
    current_chars = input()
    ascii_value = ord(current_chars)
    total_sum += ascii_value

print(f"The sum equals: {total_sum}")
