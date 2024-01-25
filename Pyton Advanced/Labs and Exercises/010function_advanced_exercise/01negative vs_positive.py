number = input().split()

positive_nums = []
negative_nums = []

for num in number:
    num = int(num)
    if num > 0:
        positive_nums.append(num)

    else:
        negative_nums.append(num)

print(sum(negative_nums))
print(sum(positive_nums))

if abs(sum(negative_nums)) > sum(positive_nums):
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")

