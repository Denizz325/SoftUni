first_sequences = input().split(", ")
second_sequences = input().split(", ")
substring = []

for first_string in first_sequences:
    for second_string in second_sequences:
        if first_string in second_string:
            substring.append(first_string)
            break

print(substring)
