string = input()
dictionary = {}
split_string = string.split(" | ")

for word in split_string:
    ll = word.split(": ")
    word = ll[0]
    definition = ll[1]
    if word not in dictionary:
        dictionary[word] = []
    dictionary[word] += [definition]

words_for_test = input().split(" | ")
command = input()

if command == "Test":
    for word_to_search in words_for_test:
        if word_to_search in dictionary:
            word_definitions = dictionary[word_to_search]
            print(f"{word_to_search}:")
            for item in word_definitions:
                print(f"-{item}")


elif command == "Hand Over":
    for key in dictionary.keys():
        print(key, end=" ")



