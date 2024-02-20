list_with_int= list(map(int, input().split(", ")))

non_zero_list = []
zero_list = []

for num in list_with_int:
    if num == 0:
        zero_list.append(num)
    else:
        non_zero_list.append(num)


result_list = non_zero_list + zero_list

print(result_list)
