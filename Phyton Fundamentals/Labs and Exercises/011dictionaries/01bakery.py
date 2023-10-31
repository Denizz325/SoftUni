table_of_stock = input().split()
bakery = {}

for i in range(0, len(table_of_stock), 2):
    key = table_of_stock[i]
    value = table_of_stock[i + 1]
    bakery[key] = int(value)

print(bakery)
