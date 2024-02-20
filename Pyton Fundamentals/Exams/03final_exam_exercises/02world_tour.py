def add_stop(stops, index, next_stop):
    index = int(command[1])
    if 0 <= index < len(stops):
        next_stop = command[2]
        stops = stops[:index] + next_stop + stops[index:]
    print(stops)
    return stops


def remove_stop(stops, start_index, stop_index):
    start_index = int(start_index)
    stop_index = int(stop_index)

    if 0 <= start_index < len(stops) and 0 <= stop_index < len(stops):
        stops = stops[:start_index] + stops[stop_index + 1:]
    print(stops)
    return stops


def switch(stops, old_stop, new_stop):
    old_stop = command[1]
    new_stop = command[2]
    if old_stop in stops:
        stops = stops.replace(old_stop, new_stop)
    print(stops)
    return stops


starting_point = input()

command_data = input()

while command_data != "Travel":
    command = command_data.split(":")
    action = command[0]

    if action == "Add Stop":
        starting_point = add_stop(starting_point, command[1], command[2])

    elif action == "Remove Stop":
        starting_point = remove_stop(starting_point, command[1], command[2])

    elif action == "Switch":
        starting_point = switch(starting_point, command[1], command[2])

    command_data = input()

print(f"Ready for world tour! Planned stops: {starting_point}")
