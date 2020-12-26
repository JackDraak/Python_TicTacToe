# Tic Tac Toe
# the classic children's game
# Jack Draak 2020


def init_grid():
    return [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"],
    ]


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


def play_game():
    this_grid = init_grid()
    game_over = False
    turn = 0

    while game_over is not True:
        turn += 1
        if turn % 2 == 0:
            player = "O"
        else:
            player = "X"
        make_a_play(player, this_grid)
        game_status = check_for_win(this_grid)
        game_over = game_status[0]
        if game_status[1] != "A":
            print("The Winner is: " + game_status[1])
            display(this_grid)


def make_a_play(player, game_board):
    valid_play = False
    while not valid_play:
        display(game_board)
        this_play = input("Player, " + player + "'s turn. Please enter the number of the cell you would like to play: ")
        if this_play.isdigit():
            cell = int(this_play)
            if 0 < cell < 10:
                for row in range(3):
                    for column in range(3):
                        if game_board[row][column] == str(cell):
                            game_board[row][column] = player
                            valid_play = True
                if not valid_play:
                    print("It looks like cell " + str(cell) + " is occupied")


def check_for_win(grid):
    game_over = False
    winner = "A"
    threat_x = 0
    threat_o = 0
    warn_x = 0
    warn_o = 0

    # Check rows
    for x in range(3):
        if count("X", grid[x]) == 3:
            game_over = True
            winner = "X"
        if count("O", grid[x]) == 3:
            game_over = True
            winner = "O"
        if count("X", grid[x]) == 2:
            threat_x = x
        if count("O", grid[x]) == 2:
            threat_o = x
        if count("X", grid[x]) == 1:
            warn_x = x
        if count("O", grid[x]) == 1:
            warn_o = x

        # TODO: get check of columns working and add check for "O"
        col = 0
        for y in range(3):
            if count("X", grid[x][y]) > 0:
                col += 1
        if col == 3:
            game_over = True

    # TODO: check diagonals, for both "X" and "O"

    # TODO: check if all cells have been played
    return game_over, winner, threat_x, warn_x, threat_o, warn_o


def count(this, array):
    this_count = 0
    for item in array:
        if item == this:
            this_count += 1
    return this_count


if __name__ == '__main__':
    play_game()
