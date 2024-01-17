odd_set = set()
even_set = set()


for num in range(1, int(input()) + 1):
    name_into_digit = sum(ord(char) for char in input()) // num
    if name_into_digit % 2 == 0:
        even_set.add(name_into_digit)
    else:
        odd_set.add(name_into_digit)

sum_odd_set, sum_even_set = sum(odd_set), sum(even_set)

if sum_even_set == sum_odd_set:
    print(*odd_set.union(even_set), sep=", ")
elif sum_even_set < sum_odd_set:
    print(*odd_set.difference(even_set), sep=", ")
else:
    print(*odd_set.symmetric_difference(even_set), sep=", ")