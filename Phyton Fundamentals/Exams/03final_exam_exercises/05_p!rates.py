def add_cities(cities, city, population, gold):
    if city not in cities:
        cities[city] = {'population': population, 'gold': gold}
    elif city in cities.keys():
        cities[city]['population'] += population
        cities[city]['gold'] += gold


def process_commands():
    command = input()
    cities = {}
    while command != "Sail":
        command = command.split("||")
        city = command[0]
        population = int(command[1])
        gold = int(command[2])
        add_cities(cities, city, population, gold)
        command = input()


process_commands()