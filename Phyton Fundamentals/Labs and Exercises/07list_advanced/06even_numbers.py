def find_index_of_even_num():
    numbers = list(map(int, input().split(", ")))
    index_list = []

    for index, value in enumerate(numbers):
        if value % 2 == 0:
            index_list.append(index)
    return index_list

print(find_index_of_even_num())