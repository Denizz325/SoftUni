from collections import deque

total_food = int(input())

orders = deque([int(x) for x in input().split()])

print(max(orders))

for order in orders.copy():
    if total_food >= order:
        orders.popleft()
        total_food -= order

    else:
        print(f"Orders left:", *orders)
        break

else:
    print("Orders complete")