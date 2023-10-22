
vehicles_tax_to_be_paid = input().split(">>")
total_tax = 0
for current_car in vehicles_tax_to_be_paid:
    tax = 0

    splited_car = current_car.split()

    type_of_car =splited_car[0]
    years_to_be_paid = int(splited_car[1])
    km_passed = int(splited_car[2])

    if type_of_car == "family":
        tax += 50
        for current_year in range(years_to_be_paid):
            tax -= 5
        i = km_passed // 3000
        tax += i * 12
        print(f"A {type_of_car} car will pay {tax:.2f} euros in taxes.")
        total_tax += tax
    elif type_of_car == "heavyDuty":
        tax += 80
        for current_year in range(years_to_be_paid):
            tax -= 8
        i = km_passed // 9000
        tax += i * 14
        print(f"A {type_of_car} car will pay {tax:.2f} euros in taxes.")
        total_tax += tax
    elif type_of_car == "sports":
        tax += 100
        for current_year in range(years_to_be_paid):
            tax -= 9
        i = km_passed // 2000
        tax += i * 18

        print(f"A {type_of_car} car will pay {tax:.2f} euros in taxes.")

        total_tax += tax


    else:
        print("Invalid car type.")

print(f"The National Revenue Agency will collect {total_tax:.2f} euros in taxes.")