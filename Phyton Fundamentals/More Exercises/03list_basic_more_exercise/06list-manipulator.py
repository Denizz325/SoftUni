#Моя код който не работи

numbers = [int(num) for num in input().split()]
normal_command = input()

even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

while normal_command != "end":
    command = normal_command.split()
    if command[0] == "exchange":
        index = int(command[1])
        if index < 0 or index >= len(numbers):
            print("Invalid index")
        else:
            part1 = numbers[:index + 1]
            part2 = numbers[index + 1:]
            numbers = part2 + part1

    elif command[0] == "max":
        if command[1] == "even":
            if even_numbers:
                max_even = max(numbers)
                index = numbers.index(max_even)
                print(index )
            else:
                print("No matches")
        if command[1] == "odd":
            if odd_numbers:
                max_odd = max(numbers)
                index = numbers.index(max_odd)
                print(index)
            else:
                print("No matches")

    elif command[0] == "min":
        if command[1] == "even":
            if even_numbers:
                min_even = min(numbers)
                index = numbers.index(min_even)
                print(index)
            else:
                print("No matches")
        if command[1] == "odd":
            if odd_numbers:
                min_odd = min(numbers)
                index = numbers.index(min_odd)
                print(index)
            else:
                print("No matches")

    elif command[0] == "first":
        count = int(command[1])
        if count > len(numbers):
            print("Invalid count")
        if command[2] == "even":
            if count == 0:
                print("[]")
            even_numbers = []
            for num in numbers:
                if num % 2 == 0:
                    even_numbers.append(num)
            print(even_numbers[:count])

        else:# одд
            if count == 0:
                print("[]")
            odd_numbers = []
            for num in numbers:
                if num % 2 != 0:
                    odd_numbers.append(num)
            print(odd_numbers[:count])

    elif command[0] == "last":
        count = int(command[1])
        if count > len(numbers):
            print("Invalid count")
        if command[2] == "even":
            if count == 0:
                print("[]")
            even_numbers = []
            for num in numbers:
                if num % 2 == 0:
                    even_numbers.append(num)
            print(even_numbers[:count])

        else:  # одд
            if count == 0:
                print("[]")
            odd_numbers = []
            for num in numbers:
                if num % 2 == 0:
                    odd_numbers.append(num)
            print(odd_numbers[:count])
    normal_command = input()
print(numbers)


# На AI кода който работи
initial_list = list(map(int, input().split()))

while True:
    command = input()
    if command == "end":
        break

    parts = command.split()
    if parts[0] == "exchange":
        index = int(parts[1])
        if 0 <= index < len(initial_list):
            first_part = initial_list[:index + 1]
            second_part = initial_list[index + 1:]
            initial_list = second_part + first_part
        else:
            print("Invalid index")
    elif parts[0] == "max" or parts[0] == "min":
        is_even = "even" in command
        max_value = float("-inf")
        max_index = -1
        min_value = float("inf")
        min_index = -1
        for i in range(len(initial_list)):
            if (is_even and initial_list[i] % 2 == 0) or (not is_even and initial_list[i] % 2 != 0):
                if initial_list[i] >= max_value:
                    max_value = initial_list[i]
                    max_index = i
                if initial_list[i] <= min_value:
                    min_value = initial_list[i]
                    min_index = i
        if max_index == -1 and min_index == -1:
            print("No matches")
        elif parts[0] == "max":
            print(max_index)
        else:
            print(min_index)
    elif parts[0] == "first" or parts[0] == "last":
        count = int(parts[1])
        if count > len(initial_list):
            print("Invalid count")
        else:
            is_even = "even" in parts[2]
            elements = []
            if parts[0] == "first":
                for i in initial_list:
                    if (is_even and i % 2 == 0) or (not is_even and i % 2 != 0):
                        elements.append(i)
                    if len(elements) == count:
                        break
            else:
                for i in reversed(initial_list):
                    if (is_even and i % 2 == 0) or (not is_even and i % 2 != 0):
                        elements.insert(0, i)
                    if len(elements) == count:
                        break
            print(elements)

print(initial_list)
