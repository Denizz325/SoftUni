shopping_list = input().split("!")
a = 0
while True:
    command = input()

    if command == 'Go Shopping!':
        break

    splited_command = command.split()
    action = splited_command[0]
    if action == "Urgent":
        item = splited_command[1]
        if item not in shopping_list:
            shopping_list.insert(0, item)
    elif action == "Unnecessary":
        item = splited_command[1]
        if item in shopping_list:
            shopping_list.remove(item)
    elif action == "Correct":
        old_item = splited_command[1]
        new_item = splited_command[2]
        if old_item in shopping_list:
            index = shopping_list.index(old_item)
            shopping_list[index] = new_item
    elif action == "Rearrange":
        item = splited_command[1]
        if item in shopping_list:
            shopping_list.remove(item)
            shopping_list.append(item)

print(', '.join(shopping_list))