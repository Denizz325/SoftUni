letters = input()
final_str = ""
last_letter = ""

for current_char in letters:
    if current_char != last_letter:
        final_str += current_char
        last_letter = current_char


print(final_str)