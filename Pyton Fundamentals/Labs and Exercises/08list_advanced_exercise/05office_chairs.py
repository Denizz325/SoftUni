#Без матрица с

row1 = list(map(int, input().split()))
row2 = list(map(int, input().split()))
row3 = list(map(int, input().split()))

winner = ""

for row in [row1, row2, row3]:
    if row.count(1) == 3:
        winner = "first_player"
    elif row.count(2) == 3:
        winner = "second_player"


for col in range(3):
    if row1[col] == row2[col] == row3[col] == 1:
        winner = "first_player"
    elif row1[col] == row2[col] == row3[col] == 2:
        winner = "second_player"


if row1[0] == row2[1] == row3[2] == 1 or row1[2] == row2[1] == row3[0] == 1:
    winner = "first_player"
elif row1[0] == row2[1] == row3[2] == 2 or row1[2] == row2[1] == row3[0] == 2:
    winner = "second_player"

if winner == "first_player":
    print("First player won")
elif winner == "second_player":
    print("Second player won")
else:
    print("Draw!")

