first_string = input()
second_string = input()

while first_string in second_string:
    second_string = second_string.replace("ice", "")

print(second_string)