num = int(input())

water_counter = 0
tank_capacity = 255

for i in range(num):
    liters_receive = int(input())

    if tank_capacity - liters_receive < 0:
        print("Insufficient capacity!")
        continue

    tank_capacity -= liters_receive
    water_counter += liters_receive


print(water_counter)

