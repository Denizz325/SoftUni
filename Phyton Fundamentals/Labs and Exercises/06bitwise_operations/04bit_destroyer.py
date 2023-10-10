number = int(input())
position = int(input())

mask = 1 << position
mask = ~ mask

result = number & mask

print(result)