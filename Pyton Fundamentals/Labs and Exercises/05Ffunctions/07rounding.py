def rounding(number):
    for num in list_of_nums:
        rounded_nums.append(round(num))
    return rounded_nums

list_of_nums = list(map(float, input().split(" ")))

rounded_nums = []
print(rounding(rounded_nums))