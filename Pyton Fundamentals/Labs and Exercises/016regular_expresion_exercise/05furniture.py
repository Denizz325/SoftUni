import re
command = input()

bought_furniture = []
total_money_spend = 0
pattern = r'>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)'

while command != "Purchase":
    match = re.search(pattern, command)
    if match:
        furniture, price, quantity = match.groups()
        bought_furniture.append(furniture)
        total_money_spend += float(price) * int(quantity)

    command = input()

print("Bought furniture:")

for furniture in bought_furniture:
    print(furniture)

print(f"Total money spend: {total_money_spend:.2f}")
