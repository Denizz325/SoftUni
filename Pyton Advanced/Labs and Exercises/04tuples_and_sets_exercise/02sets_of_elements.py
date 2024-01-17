num = input().split()

first_n_nums = set()
second_n_nums = set()

first_half = int(num[0])
second_half = int(num[1])
for _ in range(first_half):
    numbers = int(input())
    first_n_nums.add(numbers)

for _ in range(second_half):
    numbers = int(input())
    second_n_nums.add(numbers)

print(*first_n_nums & second_n_nums)





