number = int(input())

shifted_number = number >> 1

lsb = shifted_number & 1

print(lsb)