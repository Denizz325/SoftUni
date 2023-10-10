number = int(input())
position = int(input())

shifted_number = number >> position
lsb = shifted_number & 1

print(lsb)