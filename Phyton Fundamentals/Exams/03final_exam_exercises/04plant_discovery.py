def add_plants_info(plants, plant, rarity):
    plants[plant] = {'rarity': rarity, 'ratings': []}


def rate_plant(plants, plant, rating):
    if plant in plants:
        plants[plant]['ratings'].append(rating)
    else:
        print("error")


def update_rarity(plants, plant, new_rarity):
    if plant in plants:
        plants[plant]['rarity'] = new_rarity
    else:
        print("error")


def reset_ratings(plants, plant):
    if plant in plants:
        plants[plant]['ratings'] = []
    else:
        print("error")


def print_exhibition(plants):
    print("Plants for the exhibition:")
    for plant, data in plants.items():
        rarity = data['rarity']
        ratings = data['ratings']
        average_rating = 0 if not ratings else sum(ratings) / len(ratings)
        print(f"- {plant}; Rarity: {rarity}; Rating: {average_rating:.2f}")


def process_commands():
    n = int(input())
    plants = {}

    for _ in range(n):
        data = input().split("<->")
        plant = data[0]
        rarity = int(data[1])
        add_plants_info(plants, plant, rarity)

    while True:
        command = input()
        if command == "Exhibition":
            break

        tokens = command.split(": ")
        action = tokens[0]

        if action == "Rate":
            plant, rating = tokens[1].split(" - ")
            rating = int(rating)
            rate_plant(plants, plant, rating)

        elif action == "Update":
            plant, new_rarity = tokens[1].split(" - ")
            new_rarity = int(new_rarity)
            update_rarity(plants, plant, new_rarity)

        elif action == "Reset":
            plant = tokens[1]
            reset_ratings(plants, plant)

    print_exhibition(plants)


process_commands()
