n = int(input())

game_board = []
gambler_pos = []
money = 100

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(n):
    game_board.append(list(input()))

    if "G" in game_board[row]:
        gambler_pos = [row, game_board[row].index("G")]
        game_board[row][gambler_pos[1]] = '-'

command = input()

while command != "end":
    a = 0

    row, col = gambler_pos[0] + directions[command][0], gambler_pos[1] + directions[command][1]

    if not (0 <= row < n and 0 <= col < n):
        print("Game over! You lost everything!")
        break

    gambler_pos = [row, col]
    position = game_board[row][col]
    game_board[row][col] = '-'

    if position == "W":
        money += 100

    elif position == "J":
        money += 100000
        print("You win the Jackpot!")
        print(f"End of the game. Total amount: {money}$")
        game_board[gambler_pos[0]][gambler_pos[1]] = 'G'
        print(*[''.join(row) for row in game_board], sep='\n')
        break

    elif position == "P":
        money -= 200
        if money <= 0:
            print("Game over! You lost everything!")
            break

    command = input()



else:
    game_board[gambler_pos[0]][gambler_pos[1]] = 'G'
    print(f"End of the game. Total amount: {money}$")
    print(*[''.join(row) for row in game_board], sep='\n')