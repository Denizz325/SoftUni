def move_func(direction, steps):
    r = my_pos[0] + (directions[direction][0] * steps)
    c = my_pos[1] + (directions[direction][1] * steps)

    if not (0 <=  r < size and 0 <= c < size):
        return my_pos
    if field[r][c] == "x":
        return my_pos
    else:
        return [r, c]


def shoot_func(direction):
    r =  my_pos[0] + directions[direction][0]
    c = my_pos[1] + directions[direction][1]

    while 0 <= r < size and 0<= c < size:
        if field[r][c] ==  "x":
            field[r][c] = "."
            return [r, c]

        r += directions[direction][0]
        c += directions[direction][1]


size = 5

field = []

total_target = 0
target_hits = 0
target_down_poss = []
target_hit_pos = []

my_pos = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    field.append(input().split())

    if 'A' in field[row]:
        my_pos = [row, field[row].index('A')]

    total_target += field[row].count("x")


for _ in range(int(input())):
    command_info = input().split()

    if command_info[0] == "shoot":
        my_pos = move_func(command_info[1], int(command_info[2]))

    elif command_info[0] == "move":
        target_down_poss = shoot_func(command_info[1])

        if target_down_poss:
            target_hit_pos.append(target_down_poss)
            target_hits += 1

        if target_hits == total_target:
            print(f"Training completed! All {total_target} targets hit.")
            break

else:
    print(f"Training not completed! {total_target - target_hits} targets left.")

print(*target_hit_pos, sep="\n")




