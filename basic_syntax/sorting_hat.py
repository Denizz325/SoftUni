name = input()

while name != "Welcome!":

    how_long = len(name)

    if name == "Voldemort":
        print("You must not speak of that name!")
        break

    if how_long < 5:
        print(f"{name} goes to Gryffindor.")
    elif how_long == 5:
        print(f"{name} goes to Slytherin.")
    elif how_long == 6:
        print(f"{name} goes to Ravenclaw.")
    else:
        print(f"{name} goes to Hufflepuff.")

    name = input()

if name == "Welcome!":
    print("Welcome to Hogwarts.")
