orders = int(input())

total_price = 0

for i in range(orders):
    price = 0
    capsule_price = float(input())
    days = int(input())
    capsule_per_day = int(input())

    if 0.01 <= capsule_price <= 100.00 and 1 <= days <= 31 and 1 <= capsule_per_day <= 2000:
        price = capsule_price * days * capsule_per_day
        total_price += price
        print(f"The price for the coffee is: ${price:.2f}")

print(f"Total: ${total_price:.2f}")