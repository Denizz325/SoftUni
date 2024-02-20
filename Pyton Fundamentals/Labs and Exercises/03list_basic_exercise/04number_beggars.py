money_as_str = input().split(", ")
beggars = int(input())

final_sums = []
money_as_int = []

for current_money in money_as_str:
    money_as_int.append(int(current_money))

start_index = 0

while start_index < beggars:
    current_beggar_sum = 0

    for current_index in range(start_index, len(money_as_int), beggars):
        current_beggar_sum += money_as_int[current_index]

    final_sums.append(current_beggar_sum)
    start_index += 1

print(final_sums)
