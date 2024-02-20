def characters_between_start_and_stop(start:str, stop:str) -> list:
    characters = []

    for current_character in range(ord(start) + 1, ord(stop)):
        characters.append(chr(current_character))
    return characters



start = input()
end = input()
my_list = []

final_result = characters_between_start_and_stop(start, end)

print(" ".join(final_result))
