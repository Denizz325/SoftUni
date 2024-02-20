item_with_prices = input().split("|")
budget = float(input())

budget_after_take_out_prices = budget
started_budget = budget
ticket_price = 150
resell_price = 0
list_with_prices = []

for current_item in item_with_prices:
    splited_items = current_item.split("->")
    product = splited_items[0]
    price = float(splited_items[1])

    if price > budget_after_take_out_prices:
        continue

    if product == "Clothes" and price <= 50:
        budget_after_take_out_prices -= price
        budget -= price
        resell_price = price * 1.40
        budget += resell_price
        list_with_prices.append(resell_price)

    elif product == "Shoes" and price <= 35:
        budget_after_take_out_prices -= price
        budget -= price
        resell_price = price * 1.40
        budget += resell_price
        list_with_prices.append(resell_price)

    elif product == "Accessories" and price <= 20.50:
        budget_after_take_out_prices -= price
        budget -= price
        resell_price = price * 1.40
        budget += resell_price
        list_with_prices.append(resell_price)


profit = budget - started_budget

# formatted_str = " ".join([f"{price:.2f}" for price in list_with_prices]) ТОва е по- късия запис на for  цикъла отдолу

formatted_prices = []

for price in list_with_prices:
    formatted_price = "{:.2f}".format(price)
    formatted_prices.append(formatted_price)


formatted_str = " ".join(formatted_prices)
print(formatted_str)
print(f"Profit: {profit:.2f}")

if budget >= ticket_price:
    print("Hello, France!")
else:
    print("Not enough money.")