def translate_func(text, charachter, replacement):
    text = text.replace(charachter, replacement)
    print(text)
    return text


def includes_func(text, str_to_search):
    if str_to_search not in text:
        print("False")
    else:
        print("True")


def start_func(text, substring):
    if text.startswith(substring):
        print("True")
    else:
        print("False")


def lowercase_func(text):
    lowercase_text = text.lower()
    print(lowercase_text)
    return lowercase_text


def findindex_func(text, char_to_find):
    last_index = text.rfind(char_to_find)
    print(last_index)


def remove_func(text, start_index, count):
    text = text[:start_index] + text[start_index + count:]
    print(text)
    return text


string = input()

command = input().split()

while command[0] != "End":
    action = command[0]

    if action == "Translate":
        char = command[1]
        replacement = command[2]
        string = translate_func(string, char, replacement)

    elif action == "Includes":
        substring = command[1]
        includes_func(string, substring)

    elif action == "Start":
        substring = command[1]
        start_func(string, substring)

    elif action == "Lowercase":
        string = lowercase_func(string)

    elif action == "FindIndex":
        char = command[1]
        findindex_func(string, char)

    elif action == "Remove":
        start_index = int(command[1])
        count = int(command[2])
        string = remove_func(string, start_index, count)

    command = input().split()