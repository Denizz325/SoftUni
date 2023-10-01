gifts = input().split()

command = input()
index_to_check = 0

while command != "No Money":
    splited_command = command.split(" ")

    if "Required" in command:
        operation = splited_command[0]
        product = splited_command[1]
        index_to_check = int(splited_command[2])
    else:
        operation = splited_command[0]
        product = splited_command[1]

    if operation == "OutOfStock":
        for i in range(len(gifts)):
            if gifts[i] == product:
                gifts[i] = None

    if operation == "Required":
        if 0 <= index_to_check < len(gifts):
            for current_index in range(len(gifts)):
                if current_index == index_to_check:
                    gifts[current_index] = product

    if operation == "JustInCase":
        if gifts:
            gifts[-1] = product


    command = input()

for i in gifts:
    if None in gifts:
        gifts.remove(None)


print(*gifts)