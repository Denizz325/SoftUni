year = int(input())
year_is_special = False

while not year_is_special:
    year += 1

    year_as_string = str(year)
    for digit in str(year_as_string):
        year_is_special = True
        if year_as_string.count(digit) != 1:
            year_is_special = False
            break

print(year)