cars = set()

for _ in range(int(input())):
    command, car_plate = input().split(", ")

    if command == "IN":
        cars.add(car_plate)

    else:
        cars.remove(car_plate)

if cars:
    for _ in cars:
        print(_)

else:
    print("Parking Lot is Empty")









