products = {}
a = 50
command = input()

while command != "buy":
    product, price, quantity = command.split()

    price = float(price)
    quantity = int(quantity)

    if product not in products:
        products[product] = [0, 0]
    products[product][0] = price
    products[product][1] += quantity

    command = input()


for product_name, (price, quantity) in products.items():
    total_price = price * quantity
    print(f"{product_name} -> {total_price:.2f}")
