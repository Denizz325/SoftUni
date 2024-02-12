def team_lineup(*args):
    countries_with_players = {}
    for player, country in args:
        if country not in countries_with_players:
            countries_with_players[country] = []
        countries_with_players[country].append(player)

    result = " "

    sorted_data = sorted(countries_with_players.items(), key=lambda x: (-len(x[1]), x[0]))

    for country, players in sorted_data:
        result += f"{country}:\n"
        for player in players:
            result += f"  -{player}\n"

    return result




print(team_lineup(
("Harry Kane", "England"),
("Manuel Neuer", "Germany"),
("Raheem Sterling", "England"),
("Toni Kroos", "Germany"),
("Cristiano Ronaldo", "Portugal"),
("Thomas Muller", "Germany")))