from collections import deque

chocolates = [int(num) for num in input().split(", ")]
milk = deque(int(num) for num in input().split(", "))

milkshake_count = 0
while milkshake_count != 5 and chocolates and milk:

    curr_choco = chocolates.pop()
    curr_milk = milk.popleft()

    if curr_choco and curr_milk <= 0:
        continue

    elif curr_choco <= 0:
        milk.appendleft(curr_milk)
        continue
    elif curr_milk <= 0:
        chocolates.append(curr_choco)
        continue

    elif curr_milk == curr_choco:
        milkshake_count += 1

    else:
        milk.append(curr_milk)
        chocolates.append(curr_milk - 5)

if milkshake_count == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join(str(x) for x in chocolates) or 'empty'}")
print(f"Milk: {', '.join(str(x) for x in milk) or 'empty'}")