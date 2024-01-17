first_sequence = set(int(num) for num in input().split())
second_sequence = set(int(num) for num in input().split())

for _ in range(int(input())):
    data = input().split()
    command = data[0]

    if command == "Add":
        command_2 = data[1]
        numbers = set(int(x) for x in data[2:])
        if command_2 == "First":
            first_sequence.update(numbers)
        elif command_2 == "Second":
            second_sequence.update(numbers)

    elif command == "Remove":
        command_2 = data[1]
        numbers = set(int(x) for x in data[2:])
        if command_2 == "First":
            first_sequence.difference_update(numbers)
        elif command_2 == "Second":
            second_sequence.difference_update(numbers)

    elif command == "Check":
        is_subset = first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence)
        print(is_subset)

final_first_sequence = sorted(list(first_sequence))
final_second_sequence = sorted(list(second_sequence))
print(", ".join(str(i) for i in final_first_sequence))
print(", ".join(str(i) for i in final_second_sequence))  