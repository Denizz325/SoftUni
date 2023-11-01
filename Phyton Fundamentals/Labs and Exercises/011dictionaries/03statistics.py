stock = {}

while True:
    line = input()

    if line == "statistics":
        break

    food, quantity = line.split(": ")
    quantity = int(quantity)

    if food in stock:
        stock[food] += quantity

    else:
        stock[food] = quantity

product_count = len(stock)
total_quantity = sum(stock.values())

print("Products in stock:")

for product, quantity in stock.items():
    print(f"- {product}: {quantity}")

print(f"Total Products: {product_count}")
print(f"Total Quantity: {total_quantity}")