numbers = [int(num) for num in input().split()]
command = input().split()

even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

while command != "end":
    if command[0] == "exchange":
        index = int(command[1])
        if index < 0 or index >= len(numbers):
            print("Invalid index")
        else:
            part1 = numbers[:index]
            part2 = numbers[index:]
            swapped_list = part2 + part1

    elif command[0] == "max":
        if command[1] == "even":
            if even_numbers:
                max_even = max(even_numbers) - 1
                print(max_even)
            else:
                print("No matches")
        if command[1] == "odd":
            if odd_numbers:
                max_even = max(odd_numbers) - 1
                print(max_even)
            else:
                print("No matches")

    elif command[0] == "min":
        if command[1] == "even":
            if even_numbers:
                min_even = min(even_numbers) - 1
                print(min_even)
            else:
                print("No matches")
        if command[1] == "odd":
            if odd_numbers:
                min_even = min(odd_numbers) - 1
                print(min_even)
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
            print(even_numbers[:2])

        else:# одд
            if count == 0:
                print("[]")
            odd_numbers = []
            for num in numbers:
                if num % 2 == 0:
                    odd_numbers.append(num)
            print(odd_numbers[:2])

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
            print(even_numbers[:2])

        else:  # одд
            if count == 0:
                print("[]")
            odd_numbers = []
            for num in numbers:
                if num % 2 == 0:
                    odd_numbers.append(num)
            print(odd_numbers[:2])

print(numbers)
