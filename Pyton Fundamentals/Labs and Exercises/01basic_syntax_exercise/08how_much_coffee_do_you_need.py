# 1vi variant

command = input()

coffee_count = 0

while command != "END":

    if command == "coding" or command == "cat" or command == "dog" or command == "movie":
        coffee_count += 1
    elif command == "CODING" or command == "CAT" or command == "DOG" or command == "MOVIE":
        coffee_count += 2

    command = input()

if coffee_count > 5:
    print("You need extra sleep")

else:
    print(coffee_count)

#2ri variant


coffee_counter = 0
command = input()
while command != "END":
    if command.lower() == "coding" \
            or command.lower() == "dog" \
            or command.lower() == "cat" \
            or command.lower() == "movie":
        if command.islower():
            coffee_counter += 1
        else: # if command.isupper()
            coffee_counter += 2
    command = input()
if coffee_counter > 5:
    print("You need extra sleep")
else:
    print(coffee_counter)
