def take_odd(password):
    new_password = password[1::2]
    print(new_password)
    return new_password


def cut(password, index, length):
    index = int(index)
    length = int(length)
    substring = password[index:index + length]
    password = password.replace(substring, '', 1)
    print(password)
    return password


def substitute(password, substring, substitute):
    if substring in password:
        password = password.replace(substring, substitute)
        print(password)
    else:
        print("Nothing to replace!")
    return password


raw_password = input()
command = input()

while command != "Done":

    command_data = command.split()
    action = command_data[0]

    if action == "TakeOdd" :
        raw_password = take_odd(raw_password)
    elif action == "Cut":
        raw_password = cut(raw_password, command_data[1], command_data[2])

    elif action == "Substitute":
        raw_password = substitute(raw_password, command_data[1], command_data[2])

    command = input()

print(f"Your password is: {raw_password}")