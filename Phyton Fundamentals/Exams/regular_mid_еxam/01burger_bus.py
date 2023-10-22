number_of_cities = int(input())
profit_per_day = 0
total_profit = 0

for city in range(1, number_of_cities + 1):
    current_city = input()
    income = float(input())
    expenses = float(input())

    if city % 3 == 0:
        expenses += expenses * 0.50
        profit_per_day = income - expenses

    if city % 5 == 0:
        profit_per_day = income - expenses
        over_costs = income * 0.10
        profit_per_day -= over_costs
    else:
        profit_per_day = income - expenses
    total_profit += profit_per_day

    print(f"In {current_city} Burger Bus earned {profit_per_day:.2f} leva.")

print(f"Burger Bus total profit: {total_profit:.2f} leva.")


