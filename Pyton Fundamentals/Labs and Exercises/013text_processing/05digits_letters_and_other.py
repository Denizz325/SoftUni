text = input()

nums = ""
strings = ""
chars = ""

for char in text:
    if char.isdigit():
        nums += char
    elif char.isalpha():
        strings += char
    else:
        chars += char

print(nums)
print(strings)
print(chars)