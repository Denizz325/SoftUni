number_list = input().split()

abs_values = []

for num in number_list:
    abs_values.append(abs(float(num)))

print(abs_values)