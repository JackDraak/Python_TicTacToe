# Tic Tac Toe [in Python 3]
# the classic children's game
# Jack Draak 2020


# TODO: implement threats and warns so the computer can be the opponent
def check_for_win(grid):
    winner = ""
    players = ["X", "O"]
    winner = check_rows_columns(grid, players, winner)
    winner = check_diagonals(grid, players, winner)
    winner = check_stalemate(grid, winner)
    return winner


def check_diagonals(grid, players, winner):
    down = []
    up = []
    for i in range(3):
        down.append(grid[i][i])
        up.append(grid[abs(i - 2)][i])

    if winner == "":
        winner = check_set_for_win(up, players)
    if winner == "":
        winner = check_set_for_win(down, players)
    return winner


def check_rows_columns(grid, players, winner):
    for x in range(3):
        col = []
        for y in range(3):
            col.append(grid[y][x])

        if winner == "":
            winner = check_set_for_win(grid[x], players)
        if winner == "":
            winner = check_set_for_win(col, players)
    return winner


def check_set_for_win(col, players):
    winner = ""
    for player in players:
        if count(player, col) == 3:
            winner = player
    return winner


def check_stalemate(grid, winner):
    if winner == "":
        open_cells = 0
        for x in range(3):
            for y in range(3):
                if grid[x][y].isdigit():
                    open_cells += 1
                    break
        if open_cells == 0:
            winner = "stalemate"
    return winner


def count(this, array):
    this_count = 0
    for item in array:
        if item == this:
            this_count += 1
    return this_count


def display(grid):
    for x in range(3):
        print("\t", end="")
        for y in range(3):
            print(grid[x][y], end=" ")
            if y != 2:
                print(" | ", end=" ")
        if x != 2:
            print()
            print("\t--------------")
    print()


def init_grid():
    return [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"],
    ]


def play_game():
    this_grid = init_grid()
    game_over = False
    turn = 0
    while game_over is not True:
        turn += 1
        player = player_for(turn)
        take_turn(player, this_grid)
        winner = check_for_win(this_grid)
        if winner != "":
            print("The winner is: " + winner)
            display(this_grid)
            game_over = True


def player_for(turn):
    if turn % 2 == 0:
        player = "O"
    else:
        player = "X"
    return player


def take_turn(player, grid):
    valid_play = False
    while not valid_play:
        display(grid)
        this_play = input("Player, " + player + "'s turn. Please enter the number of the cell to claim: ")
        if this_play.isdigit():
            cell = int(this_play)
            if 0 < cell < 10:
                for row in range(3):
                    for column in range(3):
                        if grid[row][column] == str(cell):
                            grid[row][column] = player
                            valid_play = True
                if not valid_play:
                    print("It looks like cell " + str(cell) + " is occupied")


if __name__ == '__main__':
    play = True
    while play:
        print()
        intention = input("Would you like to play a game of Tic-Tac-Toe? ")
        if intention[0] == "n" or intention[0] == "N":
            play = False
        else:
            play_game()
