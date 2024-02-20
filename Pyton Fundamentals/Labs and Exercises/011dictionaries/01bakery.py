table_of_stock = input().split()
bakery = {}

for i in range(0, len(table_of_stock), 2):
    food = table_of_stock[i]
    quantity = table_of_stock[i + 1]
    bakery[food] = int(quantity)

print(bakery)
