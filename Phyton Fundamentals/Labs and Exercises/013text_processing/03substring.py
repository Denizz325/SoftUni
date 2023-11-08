first_str = input()
second_str = input()

while first_str in second_str:
    second_str = second_str.replace("ice", "")

print(second_str)