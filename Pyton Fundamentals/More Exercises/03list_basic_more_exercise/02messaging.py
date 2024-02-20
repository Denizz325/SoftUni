numbers = list(map(int, input().split()))
message = input()

new_word = []
index = 0

for digit in numbers:
    for num_index in range(len(digit)):
        index += digit[num_index]
