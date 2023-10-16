def multiplication(some_command, some_str_or_digit):
    if command == "int":
        return int(some_str_or_digit) * 2
    elif command == "real":
        result = float(some_str_or_digit) * 1.5
        return f"{result:.2f}"
    elif command == "string":
        return (f"${some_str_or_digit}$")


command = input()
word_or_digit = input()

print(multiplication(command, word_or_digit))