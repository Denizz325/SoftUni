name_list = input().split(", ")

sorted_names = sorted(name_list, key=lambda names: (-len(names), names))


print(sorted_names)