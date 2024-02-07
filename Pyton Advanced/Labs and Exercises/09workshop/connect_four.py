class FullColumnError(Exception):
    pass


class InvalidColumnChoice(Exception):
    pass


ROWS = 6
COLS = 7

DIRECTION_MAPPER = {
    "left": (0, -1),
    "up": (-1, 0),
    "main_diagonal": (-1, -1),
    "second_diagonal": (-1, 1)
}


def travel_direction(coordinates, current_row, current_col, el, board):
    count = 0
    row_direction, col_direction = coordinates
    for i in range(1, 4):
        next_el_row_i = current_row + row_direction * i
        nex_el_col_i = current_col + col_direction * i

        try:
            if board[next_el_row_i][nex_el_col_i] == el:
                count += 1
            else:
                return count
        except IndexError:
            return count

def travel_opposite_direction(coordinates, current_row, current_col, el, board):
    count = 0
    row_direction, col_direction = coordinates
    for i in range(1, 4):
        next_el_row_i = current_row - row_direction * i
        nex_el_col_i = current_col - col_direction * i

        try:
            if board[next_el_row_i][nex_el_col_i] == el:
                count += 1
            else:
                return count
        except IndexError:
            return count


def is_winner(current_row_i, current_col_i, board):
    for direction, coords in DIRECTION_MAPPER.items():
        searched_el = board[current_row_i][current_col_i]
        travel_direction_count = travel_direction(coords,current_row_i, current_col_i, searched_el, board)
        travel_opposite_direction_count = travel_opposite_direction(coords,current_row_i, current_col_i, searched_el, board)

        if travel_direction_count + travel_opposite_direction_count + 1 >= 4:
            return True

    else:
        return False

def print_board(board):
    for row in board:
        print(row)


def if_valid_column(col):
    if 1 <= col <= COLS:
        return True
    raise InvalidColumnChoice


def player_move_place(col_index, board):
    for row_index in range(ROWS - 1, -1, -1):
        if board[row_index][col_index] == 0:
            return row_index
    else:
        raise FullColumnError("This column is full! Please select other one")


board = [[0 for _ in range(COLS)] for _ in range(ROWS)]

turns = 1

while True:
    player = 2 if turns % 2 == 0 else 1

    try:
        column = int(input(f"Player {player}, please choose a column"))
        if_valid_column(column)
        column_index = column - 1
        row = player_move_place(column_index, board)
        board[row][column_index] = player
        if is_winner(row, column_index, board):
            break

    except FullColumnError:
        print("This column is already full! Select other one")
        continue

    except (InvalidColumnChoice, ValueError):
        print("Invalid column. Please select number from 1 to 7")
        continue

    print_board(board)
    turns += 1


print(f"Winner is player {player}")
print_board(board)