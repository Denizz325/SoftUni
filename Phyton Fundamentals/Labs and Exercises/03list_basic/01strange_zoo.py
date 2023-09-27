my_list = []

for _ in range(3):
    data = input()
    my_list.append(data)

print(my_list[::-1])

# може и със swap-ване: my_list[0], my_list[2] = my_list[2], my_list[0]