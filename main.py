# Tic Tac Toe [in Python 3]
# the classic children's game
# Jack Draak 2020


def check_for_win(grid):
    game_over = False
    winner = ""
    # TODO: implement threats and warns so the computer can be the opponent
    threat_x = 0
    threat_o = 0
    warn_x = 0
    warn_o = 0

    # TODO: how much of this can be refactored to avoid duplication?
    # scan rows
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

        # scan columns
        col = []
        for y in range(3):
            col.append(grid[y][x])

        if count("X", col) == 3:
            game_over = True
            winner = "X"
        if count("O", col) == 3:
            game_over = True
            winner = "O"
        if count("X", col) == 2:
            threat_x = x
        if count("O", col) == 2:
            threat_o = x
        if count("X", col) == 1:
            warn_x = x
        if count("O", col) == 1:
            warn_o = x

    # TODO: check diagonals for threats and warns
    down = []
    up = []
    for i in range(3):
        down.append(grid[i][i])
        up.append(grid[abs(i - 2)][i])

    if count("X", down) == 3:
        game_over = True
        winner = "X"
    if count("O", down) == 3:
        game_over = True
        winner = "O"
    if count("X", up) == 3:
        game_over = True
        winner = "X"
    if count("O", up) == 3:
        game_over = True
        winner = "O"

    # Finally, if there is no vertical, horizontal, or diagonal winner: check for stalemate
    if not game_over:
        cell_count = 0
        for x in range(3):
            for y in range(3):
                if grid[x][y].isdigit():
                    cell_count += 1
                    break
        if cell_count == 0:
            game_over = True
            winner = "stalemate"

    # so far, 'winner' is really the only thing here we truly (some refactoring involved) need to return; threat and
    # warn system has not yet been fully thought-out, and may be entirely re-worked from it's current layout, but...
    # for now it does something semi-useful. Review again once computer opponent is working, and consider refactoring
    # potential
    return game_over, winner, threat_x, warn_x, threat_o, warn_o


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
        if game_status[1] != "":
            print("The Winner is: " + game_status[1])
            display(this_grid)
        game_over = game_status[0]


if __name__ == '__main__':
    play_game()
