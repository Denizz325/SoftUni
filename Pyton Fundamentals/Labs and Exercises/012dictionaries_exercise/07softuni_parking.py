n = int(input())
parking = {}

for i in range(n):
    command = input().split()

    if "register" in command:
        name = command[1]
        license_plate_number = command[2]
        if name not in parking:
            parking[name] = license_plate_number
            print(f"{name} registered {license_plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate_number}")

    elif "unregister" in command:
        name = command[1]
        if name not in parking:
            print(f"ERROR: user {name} not found")
        else:
            parking.pop(name)
            print(f"{name} unregistered successfully")

for username, license_plate_number in parking.items():
    print(f"{username} => {license_plate_number}")



