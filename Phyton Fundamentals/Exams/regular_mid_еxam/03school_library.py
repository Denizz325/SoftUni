book_shelf = input().split("&")


while True:
    command = input().split(" | ")
    if command[0] == 'Done':
        break
    action = command[0]

    if action == "Add Book":
        book_name = command[1]
        if book_name not in book_shelf:
            book_shelf.insert(0, book_name)
    elif action == "Take Book":
        book_name = command[1]
        if book_name in book_shelf:
            book_shelf.remove(book_name)
    elif action == "Swap Books":
        book_1 = command[1]
        book_2 = command[2]
        if book_1 in book_shelf and book_2 in book_shelf:
            index1 = book_shelf.index(book_1)
            index2 = book_shelf.index(book_2)
            book_shelf[index1], book_shelf[index2] = book_shelf[index2], book_shelf[index1]

    elif action == "Insert Book":
        book_name = command[1]
        if book_name not in book_shelf:
            book_shelf.append(book_name)
    elif action == "Check Book":
        index_to_check = int(command[1])
        if 0 <= index_to_check < len(book_shelf):
            print(book_shelf[index_to_check])

print(", ".join(book_shelf))