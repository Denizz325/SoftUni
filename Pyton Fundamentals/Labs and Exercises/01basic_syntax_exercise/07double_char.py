current_string = input()

while current_string != "End":

    if not current_string == "SoftUni":
        new_string = ""
        for charectar in current_string:
            new_string += charectar * 2
        print(new_string)

    current_string = input()