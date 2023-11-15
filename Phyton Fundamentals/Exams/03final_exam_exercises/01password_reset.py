password = input()

command = input()

while command != "Done":

    if "TakeOdd" in command:
        password = password[1::2]

    elif "Cut" in command:
        pass

    elif "Substitute" in command:
        pass

    command = input()