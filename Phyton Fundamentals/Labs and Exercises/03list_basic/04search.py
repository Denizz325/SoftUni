num_of_lines = int(input())
special_word = input()

my_list = []
my_list_with_special_word = []
lower_word = ""


for i in range(num_of_lines):
    some_string = input()

    my_list.append(some_string)

    if some_string.count(special_word) > 0:
        my_list_with_special_word.append(some_string)


print(my_list)
print(my_list_with_special_word)





