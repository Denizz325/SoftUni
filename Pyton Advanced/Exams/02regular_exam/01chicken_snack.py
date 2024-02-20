from collections import deque

money_sequence = deque(int(num) for num in input().split())
food_sequence = deque(int(num) for num in input().split())

bought_food = 0

while money_sequence and food_sequence:
    current_money = money_sequence.pop()
    current_food = food_sequence.popleft()

    if current_food > current_money:
        continue

    elif current_food == current_money:
        bought_food += 1

    elif current_money > current_food:
        bought_food += 1
        if money_sequence:
            difference = current_money - current_food
            money_sequence[-1] += difference


if not bought_food:
    print("Henry remained hungry. He will try next weekend again.")

if bought_food >= 4:
    print(f"Gluttony of the day! Henry ate {bought_food} foods.")

elif bought_food:
    if bought_food == 1:
        print(f"Henry ate: {bought_food} food.")
    else:
        print(f"Henry ate: {bought_food} foods.")




