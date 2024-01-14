clothes = [int(x) for x in input().split()]
rack_capacity = int(input())

current_rack_space = rack_capacity
used_rack = 1

while clothes:
    clothe = clothes.pop()

    if current_rack_space >= clothe:
        current_rack_space -= clothe

    else:
        used_rack += 1
        current_rack_space = rack_capacity - clothe

print(used_rack)