n = int(input())

matrix = []

enemy_jets_count = 0
jet_pos = []
armor = 300

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(n):
    matrix.append(list(input()))

    if "J" in matrix[row]:
        jet_pos = [row, matrix[row].index("J")]
        matrix[row][jet_pos[1]] = '-'
    if "E" in matrix[row]:
        enemy_jets_count += matrix[row].count("E")


a = 0

while True:

    command = input()

    if armor <= 0:
        break
    if enemy_jets_count <= 0:
        break

    row, col = jet_pos[0] + directions[command][0], jet_pos[1] + directions[command][1]
    jet_pos = [row, col]
    current_pos = matrix[row][col]

    if current_pos == "-":
        continue

    elif current_pos == "E":
        enemy_jets_count -= 1
        matrix[row][col] = "-"

        if enemy_jets_count <= 0:
            print("Mission accomplished, you neutralized the aerial threat!")
            break
        else:
            armor -= 100
            if armor <= 0:
                print(f"Mission failed, your jetfighter was shot down! Last coordinates [{row}, {col}]!")
                break

    elif current_pos == "R":
        matrix[row][col] = "-"
        armor = 300




matrix[jet_pos[0]][jet_pos[1]] = "J"
print(*[''.join(row) for row in matrix], sep='\n')