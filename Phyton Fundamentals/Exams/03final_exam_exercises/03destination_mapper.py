import re

text = input()
pattern = r'([=\/])([A-Z][a-zA-Z]{2,})\1'

travel_points = 0
destinations = []
matches = re.findall(pattern, text)

if matches:
    for match in matches:
        destinations.append(match[1])

    travel_points = sum(len(destination) for destination in destinations)

print(f'Destinations: {", ".join(destinations)}')
print(f"Travel Points: {travel_points}")
