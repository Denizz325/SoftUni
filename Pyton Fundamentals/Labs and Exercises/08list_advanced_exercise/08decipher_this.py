 #Решение на колега 1 (без функция)

secret_message = input().split()
new_message = []
for word in secret_message:
    digit, let = "", ""
    for letter in word:
        if letter.isdigit():
            digit += letter
        else:
            let += letter

    letter_for_digit = chr(int(digit))
    if len(let) != 1:
        new_word = f"{let[-1]}{let[1:-1]}{let[0]}"
    else:
        new_word = let
    new_word = letter_for_digit + new_word
    new_message.append(new_word)

print(*new_message)

#Решение на колега 2 (с функция)

def message_deciphered(string):
    deciphered = []
    for word in string:
        word = list(word)
        characters = [x for x in word if not x.isnumeric()]
        numbers = int(''.join([x for x in word if x.isnumeric()]))
        ascii_letter = chr(numbers)
        characters[0], characters[-1] = characters[-1], characters[0]
        ready_word = ascii_letter + ''.join(characters)
        deciphered.append(ready_word)
    return ' '.join(deciphered)


input_line = input().split()
print(message_deciphered(input_line))