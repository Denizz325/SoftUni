def add_cities(cities, city, population, gold):
    if city not in cities.keys():
        cities[city] = {'population': 0, 'gold': 0}

    cities[city]['population'] += population
    cities[city]['gold'] += gold


def plunder_func(cities, city, population, gold):
    print(f"{city} plundered! {gold} gold stolen, {population} citizens killed.")
    cities[city]['population'] -= population
    cities[city]['gold'] -= gold
    if cities[city]['population'] == 0 or cities[city]['gold'] == 0:
        cities.pop(city)
        print(f"{city} has been wiped off the map!")


def prosper_func(cities, city, gold):
    if gold < 0:
        print("Gold added cannot be a negative number!")
    else:
        cities[city]['gold'] += gold
        print(f"{gold} gold added to the city treasury. {city} now has {cities[city]['gold']} gold.")


def print_func(cities):
    if cities:
        print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
        for town, town_info in cities.items():
            print(f"{town} -> Population: {town_info['population']} citizens, Gold: {town_info['gold']} kg")

    else:
        print("Ahoy, Captain! All targets have been plundered and destroyed!")


def process_commands():
    cities = {}
    command = input().split("||")
    while command[0] != "Sail":
        city, population, gold = command[0], int(command[1]), int(command[2])
        add_cities(cities, city, population, gold)
        command = input().split("||")

    command = input().split("=>")
    while command[0] != "End":
        action = command[0]

        if action == "Plunder":
            town, people, gold = command[1], int(command[2]), int(command[3])
            plunder_func(cities, town, people, gold)

        elif action == "Prosper":
            town, gold = command[1], int(command[2])
            prosper_func(cities, town, gold)

        command = input().split("=>")

    print_func(cities)


process_commands()