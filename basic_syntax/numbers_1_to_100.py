#1vi variant
while True:
    number = float(input())

    if 1 <= number <= 100:
        print(f"The number {number} is between 1 and 100")
        break

#2ri varinat
number = float(input())
while number < 1 or number > 100:
    number = float(input())
print(f"The number {number} is between 1 and 100")