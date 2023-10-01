list_of_int_as_str = input().split()
nums_to_remove = int(input())
int_list = []

for current_num in list_of_int_as_str:
    int_current_num = int(current_num)
    int_list.append(int_current_num)

for current_index in range(nums_to_remove):
    int_list.remove(min(int_list))

print(*int_list, sep=", ")
