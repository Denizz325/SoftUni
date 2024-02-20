companions_count = int(input())
days = int(input())

coin_counter = 0

for current_day in range(1, days + 1):

    if current_day % 10 == 0:
        companions_count -= 2

    if current_day % 15 == 0:
        companions_count += 5

    if current_day % 3 == 0:
        coin_counter -= companions_count * 3

    if current_day % 5 == 0:
        coin_counter += companions_count * 20

        if current_day % 3 == 0:
            coin_counter -= companions_count * 2

    coin_counter += 50
    coin_counter -= companions_count * 2

coins_per_companion = coin_counter // companions_count

print(f"{companions_count} companions received {coins_per_companion} coins each.")


