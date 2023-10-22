book_shelf = input().split("&")

command = input().split(" | ")

while command[0] == 'Done':
    action = command[0]

    if action == "Add Book":
        book_name = command[1]
        if book_name not in book_shelf:
            book_shelf.insert(0, book_name)
    if action == "Take Book":
        book_name = command[1]
        if book_name in book_shelf:
            book_shelf.remove(book_name)
    if action == "Swap Book":
        old_book = command[1]
        new_book = command[2]
        book_shelf[old_book] = new_book
    if action == "Insert Book":
        book_name = command[1]
        if book_name not in book_shelf:
            book_shelf.append(book_name)
    if action == "Check Book":
        index_to_check = int(command[1])
        if 0 <= index_to_check < len(book_shelf):
            print(book_shelf[index_to_check])

print(", ".join(book_shelf))