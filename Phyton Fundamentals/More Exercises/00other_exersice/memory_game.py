def memory_game():
    sequence_of_elements = input().split()
    moves_count = 0
    while True:

        command = input()
        moves_count += 1
        if command == "end":
            print(f"Sorry you lose :(")
            print(*sequence_of_elements)
            break

        splited_command = command.split()
        index_1 = int(splited_command[0])
        index_2 = int(splited_command[1])

        if (
                index_1 == index_2
                or index_1 < 0
                or index_2 < 0
                or index_1 >= len(sequence_of_elements)
                or index_2 >= len(sequence_of_elements)
        ):
            # Вмъкваме новите стойности на средата на списъка
            middle_index = len(sequence_of_elements) // 2
            value_to_insert = f"-{moves_count}a"
            sequence_of_elements.insert(middle_index, value_to_insert)
            sequence_of_elements.insert(middle_index, value_to_insert)
            print("Invalid input! Adding additional elements to the board")
        else:
            for element in sequence_of_elements:
                if sequence_of_elements[index_1] == sequence_of_elements[index_2]:
                    print(f"Congrats! You have found matching elements - {sequence_of_elements[index_1]}!")
                    sequence_of_elements.pop(max(index_1, index_2))
                    sequence_of_elements.pop(min(index_1, index_2))
                else:
                    print("Try again!")
                break

        if not sequence_of_elements:
            print(f"You have won in {moves_count} turns!")
            break


memory_game()

