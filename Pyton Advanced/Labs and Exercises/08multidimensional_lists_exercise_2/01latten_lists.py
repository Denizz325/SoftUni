elements = input().split("|")

el_list = []

for el in elements[::-1]:
    el_list.extend(el.split())

print(*el_list)