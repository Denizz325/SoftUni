countries = input().split(", ")
capitals = input().split(", ")

final_info = {countries[index]: capitals[index]
              for index in range(len(countries))}
for country, capital in final_info.items():
    print(f"{country} -> {capital}")
